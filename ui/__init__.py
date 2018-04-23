import bpy
from ui import layers_panel


def reload():

    from importlib import reload
    reload(layers_panel)


def register():
    print("Registering", __name__)
    bpy.utils.register_module(__name__)
    layers_panel.register()


def unregister():
    print("Unregistering ", __name__)
    bpy.utils.unregister_module(__name__)
    layers_panel.unregister()
