import math
import maya.cmds as cmds
import random as random
import mtoa.utils as mutils
cmds.file(f=True,new=True)

#-----------------------------------------------------

def Scene():
    
    cmds.file(f=True,new=True)
    


# A-Création d'un shader et application du shader de base

def shaderRoute():
    
    cmds.file(f=True,new=True)

b = cmds.shadingNode('lambert', asShader=True)
cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='lambert1SG')
cmds.connectAttr('lambert1.outColor', 'lambert1SG.surfaceShader')

#ajout texture

cmds.shadingNode('file', asTexture=True)
cmds.shadingNode('place2dTexture', asUtility=True)
cmds.connectAttr( 'place2dTexture1.outUV', 'file1.uvCoord')
cmds.connectAttr('file1.outColor', 'lambert1.color')


r = random.randint(mini,maxi)

mini = 1
maxi = 40


def Route():
    
    cmds.file(f=True,new=True)

for p in range(r):
    sphereName = cmds.polyPlane(name = "route"+str(1))
    sphereName = "pPlane"+str(p+1)
    cmds.sets(edit=True, forceElement = 'lambert1SG')
    posX = p
    posZ = 0
    cmds.move(posX,posZ,xz=True)
    

