import bpy


class LayersPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "LayersPanel"
    bl_idname = "OBJECT_PT_layers_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Layers Panel!", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.operator("mesh.primitive_cube_add")


def register():
    bpy.utils.register_class(LayersPanel)


def unregister():
    bpy.utils.unregister_class(LayersPanel)


def main():
    print("Initializing", __name__)
    register()
