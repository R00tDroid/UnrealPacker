import os;
import argparse;
import json;

argument_parser = argparse.ArgumentParser()

argument_parser.add_argument('-manifest')
argument_parser.add_argument('-type', choices=['application', 'plugin'])
argument_parser.add_argument('-engine')
argument_parser.add_argument('-output')

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

print('Manifest: ' + manifest)
print('Type: ' + package_type)
print('Engine version: ' + engine_version)
print('Output directory: ' + output_directory)

exit(0)
