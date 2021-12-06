import math
import maya.cmds as cmds
import random as random


def water():
        object = cmds.polyPlane(height=10, width=10)
        print(object)
        O_shader = cmds.shadingNode('oceanShader', asShader=True)
        bs = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='oceanShader1SG')
        cmds.connectAttr(O_shader + '.outColor', bs + '.surfaceShader')
        cmds.connectAttr(O_shader + '.outColor', bs + '.displacementShader')
        O_shader2 = cmds.shadingNode('blinn', asRendering=True)
        cmds.connectAttr(O_shader + '.outColor', O_shader2 + '.transparency')

        # Régler la couleur du shader
        print(O_shader)
        cmds.select(str(object[0]))
    
        cmds.sets(edit=True, forceElement=O_shader+'SG')
        cmds.setAttr(O_shader+'.scale',5)