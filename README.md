# Blender Addon Starter Kit

This repository contains a blender addon template with some fancy features like:
* External IDE support
    * Load the dev.py file in blender and press the "Run Script" button to show the changes in realtime
    * Syntax highlight for bpy modules
        * Blender 2.79b API already in lib/
        * You can retrieve other APIs by running script/update_blender_api.sh (for unix only)
* You addon updates itself on startup if there is a newer version in github or other VCS

# Getting this code in use
## Linux/Unix
1. Fork this repository (if you wanna keep your changes on github)
2. Clone the forked repo or this repo on your working machine
3. OPTIONAL STEP!!! if you are gonna use blender 2.79b skip this step.
   run ./update_blender_api.sh in scripts/ to retrieve the python blender APIs from your blender installation
4. Add blender lib to all your pycharm projects (in order to have bpy modules autocompletation in the IDE)
    * File > Settings
    * Project: PROJECT_NAME > Project Interpreter
    * Click the gear icon in the right upper corner of the window
    * Click "Show All"
    * Click the icon "Show Paths For The Selected Interpreter"
    * Click the green + icon
    * Add the lib/blender directory to the list
   ![pycharm](https://github.com/mutantbob/pycharm-blender/blob/master/pycharm-3.4-screenshot.png?raw=true)
5. Open dev.py in blender
6. Edit the git_path var to point to the path of your plugin eg: /home/gnuton/git/blendaddon/
7. Now you can change stuff in your code
8. Press "Run Script" in blender to run it.
9. updater is off by default and needs some configuration to work. Edit helpers/updater.py var to take it in use

# Windows
Same as above, but as for now batch script for retrieving blender python API is missing.
