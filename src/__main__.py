import maya.cmds as cmds
import sys
cmds.file(f=True, new=True)


def importMayaScript(nameFolder):
    
    myScriptDir = cmds.internalVar(userScriptDir=True)
    setScriptDir = myScriptDir+'generative-city/src/'+str(nameFolder)+'/'
    sys.path.append(setScriptDir)
    
importMayaScript("env")
importMayaScript("element")

from Terrain_hexagon_gen import *
from Batiment_position import *

#from nuage import *
from importMesh import ManageImport , openTextureFile
from batt import Element


"""-----------Ne pas toucher les imports ----------------"""


if __name__ == '__main__':
    vert1 = createShader("blinn", [0,0.6,0], "bitumeVert")
    vert2 = createShader("blinn", [0,0.6,0.2], "bitumeVertType2")
    bleu1 = createShader("blinn", [0,0.3,0.6], "eauBleu")
    bleu2 = createShader("blinn", [0,0.4,0.6], "eauBleu2")
    bleu3 = createShader("blinn", [0,0.5,0.6], "eauBleu3")
    bitume1 = createShader("blinn", [0.19,0.19,0.19], "terreBitume")
    bitume2 = createShader("blinn", [0.1,0.1,0.1], "terreBitume2")
    bitume3 = createShader("blinn", [0.16,0.16,0.16], "terreBitume3")
    blanc = createShader("blinn", [1,1,1], "blanc")
    terrain(20,20,1,2)

    bilelBat = ManageImport("batiment_CyberPunk_uv.mb")
    bilelBat.openMayaFile()
    bilelBat.ManageObj([2,0,0],[1,1,1], [0,0,0])
    bilelBat.deleteReference()
    
    bat = Element("generativeBat",1,3,4,"basic")
    bat.building(8)
