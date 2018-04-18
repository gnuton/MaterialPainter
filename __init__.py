from ui import panel
import bpy

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

# Requires Python >= 3.4
if bpy.__name__ in locals():
    from importlib import reload
    if "panel" in locals():
        reload(panel)

if __name__ == "__main__":
    print("Loading Material Painter.")
    panel.main()
