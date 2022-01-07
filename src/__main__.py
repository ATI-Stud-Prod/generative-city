import maya.cmds as cmds
import sys
import random

cmds.file(f=True, new=True)


def importMayaScript(nameFolder):
    
    myScriptDir = cmds.internalVar(userScriptDir=True)
    setScriptDir = myScriptDir+'generative-city/src/'+str(nameFolder)+'/'
    sys.path.append(setScriptDir)
    
importMayaScript("env")
importMayaScript("element")

from Terrain_hexagon_gen import *
#from Batiment_position import *

#from nuage import *
from importMesh import ManageImport , openTextureFile
from batt import Element


"""-----------Ne pas toucher les imports ----------------"""
#variable de terrain


if __name__ == '__main__':

    mairie = ManageImport("monument_CyberPunk_combine.mb")
    #
    #bat = Element("generativeBat",1,3,4, [8,0,0],"basic")
    #bat.building(8)
    terrain(10,10,0,3)
    #position des grilles
    #placementDeGrille(['terreBitume','terreBitume2','terreBitume3'])

    #positionnement des objets sur les faces
    mairie.openMayaFile()

    print(mairie.openMayaFile())
    
    mairie.openMayaFile()
    mairie.ManageObj([500,0,0],[.01,.01,.01], [0,0,0])
    

   
    