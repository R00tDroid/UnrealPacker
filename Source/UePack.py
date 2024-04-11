import os
import argparse
import json
import winreg
import sys
import subprocess

argument_parser = argparse.ArgumentParser(description='An automation tool to package Unreal Engine projects or plugins.')

argument_parser.add_argument('-manifest', help="Path to the project or plugin manifest. This is a .uproject or .uplugin file.")
argument_parser.add_argument('-type', choices=['application', 'plugin'], help="Override automatic type detection based on the manifest. This controls whether a project will be packaged, or a plugin.")
argument_parser.add_argument('-engine', help="Set the engine version to use. For projects this is automatically detected, but can be overridden. For plugins this argument is required.")
argument_parser.add_argument('-output', help="Output directory where the package will be generated.")
argument_parser.add_argument('-platform', default="Win64", help="Target platform. Only required for projects.")
argument_parser.add_argument('-config', default="Shipping", help="Target configuration. Only required for projects.")

if len(sys.argv) == 1:
    argument_parser.print_help(sys.stderr)
    exit(1)

arguments = argument_parser.parse_args()

if arguments.manifest is None:
    print('Project/plugin manifest path not set')
    exit(-1)

manifest = os.path.abspath(arguments.manifest)

if not os.path.isfile(manifest):
    print('Could not find project/plugin manifest: ' + manifest)
    exit(-1)

if arguments.type is not None:
    package_type = arguments.type
else:
    manfest_name, manifest_extension = os.path.splitext(manifest)
    if manifest_extension == '.uproject':
        package_type = 'application'
    elif manifest_extension == '.uplugin':
        package_type = 'plugin'
    else:
        print('Could not identify manifest type: ' + manifest_extension)
        exit(-1)

if arguments.engine is not None:
    engine_version = arguments.engine
elif package_type == 'application':
    manifest_file = open(manifest, 'r')
    manifest_json = json.loads(manifest_file.read())
    engine_version = manifest_json['EngineAssociation']
else:
    print('Could not engine version')
    exit(-1)

if arguments.output is not None:
    output_directory = os.path.abspath(arguments.output)
else:
    output_directory = os.getcwd()

try:
    engine_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\EpicGames\\Unreal Engine\\' + engine_version, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
    engine_location = engine_installed = winreg.QueryValueEx(engine_key, 'InstalledDirectory')[0]
    winreg.CloseKey(engine_key)
except Exception as ex:
    print('Could not find UE' + engine_version)
    exit(-1)

print('Manifest: ' + manifest)
print('Type: ' + package_type)
print('Engine version: ' + engine_version)
print('Engine location: ' + engine_location)
print('Output directory: ' + output_directory)

uat_path = engine_location + '\\Engine\\Build\\BatchFiles\\RunUAT.bat'

command = '"' + uat_path + '"'

if package_type == 'application':
    command += ' BuildCookRun'
    command += ' -project="' + manifest + '"'
    command += ' -platform="' + arguments.platform + '"'
    command += ' -clientconfig="' + arguments.config + '"'
    command += ' -serverconfig="' + arguments.config + '"'
    command += ' -noP4'
    command += ' -Compressed'
    command += ' -cook'
    command += ' -allmaps'
    command += ' -build'
    command += ' -stage'
    command += ' -pak'
    command += ' -archive'
    command += ' -prereqs'
    command += ' -archivedirectory="' + output_directory + '"'

elif package_type == 'plugin':
    command += ' BuildPlugin'
    command += ' -Plugin="' + manifest + '"'
    command += ' -Package="' + output_directory + '"'
    command += ' -CreateSubFolders'

print(command)

return_code = subprocess.call(command, shell=False)
exit(return_code)
