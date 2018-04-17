# Blender Addon Template
This repository contains a blender addon template with some fancy features like:
* Code in an external IDE (eg pycharm) and display the changes straightaway in Blender
* IDE support for blender python API
* Script for updating the blender python API
* Blender python API 2.79b already in lib/

# How to use
## Linux/Unix
1. Fork this repository (if you wanna keep your changes on github)
2. Clone the forked repo or this repo
3. OPTIONAL since in lib/blender you can already find 2.79b files.
   But in case you wanna use a different blender files:
   run ./update_blender_api.sh in scripts/ to retrieve the python blender APIs from your blender installation
4. Add blender lib to all your pycharm projects:
    * File > Settings
    * Project: PROJECT_NAME > Project Interpreter
    * Click the gear icon in the right upper corner of the window
    * Click "Show All"
    * Click the icon "Show Paths For The Selected Interpreter"
    * Click the green + icon
    * Add the lib/blender directory to the list
   ![pycharm](https://github.com/mutantbob/pycharm-blender/blob/master/pycharm-3.4-screenshot.png?raw=true)
5. Open dev.py in blender
6. Edit the line git_path with the path to your plugin eg: /home/gnuton/git/blendaddon/
7. Make your changes in pycharm
8. Press "Run Script" in blender to run it.

# Windows
Same as above, but as for now batch script for retrieving blender python API is missing.
