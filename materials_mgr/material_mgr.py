import bpy

"""
    tree = bpy.context.object.active_material.node_tree
    nodes = tree.nodes
    links = tree.links
"""
class MaterialMgr:
    def __init__(self):
        pass

    def deselect_all_nodes:
        """Returns {'FINISHED'} if everything whent fine, False if failure"""
        for area in bpy.context.screen.areas:
            if area.type == "NODE_EDITOR":
                override = {'screen': bpy.context.screen, 'area': area}
                return bpy.ops.node.select_all(override, action='DESELECT')
        return False

    @staticmethod
    def get_material_by_name(name):
        """Returns the material associated with name. Returns None if any"""
        try:
            return bpy.data.materials[name]
        except KeyError:
            return None

    def get_active_material(self):
        """Returns bpy.data.materials[MAT_NAME] or None"""
        return bpy.context.object.active_material

    def get_material_tree(self, mat):
        return mat.node_tree;

    def get_material_nodes(self, mat):
        """Returns the nodes in the material"""
        tree = self.get_material_tree(mat)
        return tree.nodes

    def add_node(self, mat, node_name, node_type = "ShaderNodeBsdfPrincipled", location = (0, 0)):
        """
        Adds a node to the tree. Returns the created node.
        :param mat: The material
        :param node_type: node_type: String - Any of the ShaderNode listed here https://docs.blender.org/api/blender_python_api_current/bpy.types.ShaderNode.html
        :param location: Tuple - Position of the node as shown in the node editor
        :return: the new node
        """
        nodes = self.get_material_nodes(mat)
        new_node = nodes.new(node_type)
        new_node.name = node_name
        new_node.location = location
        return new_node

    def add_group_node(self, mat, node_name, location = (0,0)):
        """
        Adds a group node to the target material
        :param mat:
        :param node_name:
        :param location:
        :return:
        """
        group = self.add_node(mat, node_name, "ShaderNodeGroup", location)
        group.node_tree = bpy.data.node_groups[node_name]
        return group

    def link_nodes(self, mat, nodeA, outputAIndex, nodeB, inputBIndex):
        """
        Links two nodes together
        :param mat: The target material
        :param nodeA: The node with the output socket
        :param outputAIndex: output socket index of the node A
        :param nodeB:  The node with the input socket
        :param inputBIndex: Input socket index of the node B
        :return: the link between the two nodes as NodeLinks object
        """
        tree = self.get_material_tree(mat)
        link = tree.links.new(nodeA.outputs[outputAIndex],nodeB.inputs[inputBIndex])
        return link

    def unlink_all_nodes(self, mat):
        """
        Unlinks all nodes
        :param mat:
        :return: None
        """
        tree = self.get_material_tree(mat)
        tree.links.clear()


    def get_material_links(self, mat):
        """Returns a list of links as NodeLink objects among material nodes"""
        tree = self.get_material_tree(mat)
        return tree.links

    def node_type(self, node):
        """
        Returns the type of the node
        :param node:
        :return: type of the node as string
        """
        return node.bl_rna.identifier

    @staticmethod
    def clear(mat):
        """Removes all nodes for the target material"""
        nodes = mat.node_tree.nodes
        for node in nodes:
            nodes.remove(node)

