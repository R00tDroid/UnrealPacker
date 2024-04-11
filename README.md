# UnrealPacker
A commandline tool to automatically package Unreal Engine projects or plugins

---

[![CodeFactor](https://www.codefactor.io/repository/github/r00tdroid/unrealpacker/badge)](https://www.codefactor.io/repository/github/r00tdroid/unrealpacker)

## Arguments
| Argument | Options | Description |
| --- | --- | --- |
| -manifest | - | Path to the project or plugin manifest. This is a .uproject or .uplugin file. |
| -type | application, plugin | Override automatic type detection based on the manifest. This controls whether a project will be packaged, or a plugin. |
| -engine | - | Set the engine version to use. For projects this is automatically detected, but can be overridden. For plugins this argument is required. |
| -output | - | Output directory where the package will be generated. |
| -platform | - | Target platform. Only required for projects. |
| -config | Debug, Development, Shipping | Target configuration. Only required for projects. |

## Examples
Packaging a game with the default settings<br>
`uepacker -manifest MyProject.uproject -output PackagedProject`

Packaging a plugin for 5.2<br>
`uepacker -manifest CoolPlugin.uplugin -output PluginVersions -engine 5.2`
