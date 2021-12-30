import maya.cmds as cmds
import sys 

def importMayaScript(nameFolder):

    myScriptDir = cmds.internalVar(userScriptDir=True)
    setScriptDir = myScriptDir+'generative-city/src/'+str(nameFolder)+'/'
    sys.path.append(setScriptDir)
    
importMayaScript("env")      
importMayaScript("element")      

from Terrain_hexagon_gen import terrain
from importMesh import ManageImport , openTextureFile
from batt import Element
"""-----------Ne pas toucher les imports ----------------"""

cmds.file(f=True, new=True)

if __name__ == '__main__':
    bilelBat = ManageImport("batiment_CyberPunk_uv.mb")
    bilelBat.openMayaFile()
    bilelBat.ManageObj([2,0,0],[1,1,1], [0,0,0])
    bilelBat.deleteReference()
    
    bat = Element("generativeBat",5,3,4,"basic")
    bat.building(4)

    
