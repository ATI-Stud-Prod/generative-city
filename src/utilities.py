import maya.cmds as cmds
import random as random


colorScheme = {
    'custom1': [128,255,0],
    'yellow': [255,255,0],
    'blue': [0,0,255],
    'red': [255, 0, 0],
    'purple': [255,0,255],
    'green': [0, 255, 0]
}


class Shader:
    def __init__(self, node_t):
        self.NodeType=node_t

    def __create_shader(self, naming, node_type):
        node_type = self.NodeType
        mtl = cmds.shadingNode(node_type, name=naming, asShader=True)
        sg = cmds.sets(name="%sSG" % naming, empty=True, renderable=True, noSurfaceShader=True)
        cmds.connectAttr("%s.outColor" % mtl, "%s.surfaceShader" % sg)
        return mtl, sg        

    def set_color(self, key_color, shader_colors):
        meshes = cmds.ls(selection=True, dag=True, type="mesh", noIntermediate=True)
        material, sgrp = self.__create_shader("siege_MTL", self.NodeType)
        cmds.setAttr(material + ".color", shader_colors[key_color][0], shader_colors[key_color][1], shader_colors[key_color][2], type='double3')
        cmds.sets(meshes, forceElement=sgrp)