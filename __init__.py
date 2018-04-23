import ui
import bpy
from autoupdater import setup as autoupdater_setup
from importlib import reload

bl_info = {
    "name": "Material Painter",
    "author": "Antonio Aloisio",
    "version": (0, 0, 1),
    "blender": (2, 7, 8),
    "location": "3D View > Tool Shelve > Mixamo Tab",
    "description": ("Experimental PBR Material painter"),
    "warning": "",  # used for warning icon and text in addons panel
    "wiki_url": "https://github.com/gnuton/MaterialPainter/wiki",
    "tracker_url": "https://github.com/enziop/MaterialPainter/issues",
    "category": "Texturing"
}


def trigger_reload(mod, locs=locals()):

    print("Reloading ", mod.__name__)
    if ui.__name__ not in locs:
        return

    try:
        mod.unregister()
    except Exception as e:
        print("Unable to unregister error:", e)

    reload(mod)

    if hasattr(mod, 'reload'):
        mod.reload()


def register():
    ui.register()

def unregister():
    ui.unregister()

if bpy.__name__ in locals():
    modules = [ui, autoupdater_setup]
    [trigger_reload(module) for module in modules]

if __name__ == "__main__":
    autoupdater_setup.init(bl_info)
    register()
