import math
import maya.cmds as cmds
import random as random
import mtoa.utils as mutils
from functools import partial

cmds.file(f=True, new=True)

def world():
    mutils.createLocator("aiSkyDomeLight", asLight=True)
    panel = cmds.getPanel(wf=1)
    cmds.modelEditor(panel, e=1, allObjects=0)
    cmds.modelEditor(panel, e=1, polymeshes=1) 
    cmds.modelEditor(panel, e=1, displayTextures=1)


def getSliderValue(ctrlName):
    value = cmds.intSlider(ctrlName, q=True, value=True)
    return value

def moveXYZ(slider, *arg, **kwargs):
    value = getSliderValue(slider)
    #cmds.duplicate(n=object,st=False)
    cmds.select()
    cmds.move(value,*arg, **kwargs)


class Env:
    def __init__(self,water, sizeX, sizeY):
        self.water = water
        self.sizeX = sizeX
        self.sizeY = sizeY

    def UI(self="UI"):
        window = cmds.window( title="Long Name", iconName='Short Name', widthHeight=(200, 800), s = False, menuBar = True)
        cmds.columnLayout( adjustableColumn=True)
        mySlider = cmds.intSlider(min=1, max=100, value=0, step=1, dc = 'empty')
        #cmds.intSlider(mySlider, e=True, dc = partial(moveXYZ, mySlider, x=1))
        slider1 = cmds.floatSliderGrp(min =0.0,max=1.0,label="BlinnRed", field= True, backgroundColor=[1,1,1])
        
        #cmds.setAttr(O_shader+'.scale',5)
        # cmds.text(label="City Width", al = "left")
        # cityWidth = cmds.textField( tx = "700")
        # progressControl = cmds.progressBar(maxValue=100, width=100, vis = False)
        
        #cmds.button(label = "Generate", c = partial(cityWidth))
        
        #show window
        cmds.showWindow(window)

    def sqSetClustersZeroScale(self, *arqs):
        if self.clusterList:
            for item in self.clusterList:
                cmds.setAttr(item+".scaleX", 0)
                cmds.setAttr(item+".scaleY", 0)
                cmds.setAttr(item+".scaleZ", 0)


    def water(self=" "):
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
        
    

Env.water()
Env.UI()