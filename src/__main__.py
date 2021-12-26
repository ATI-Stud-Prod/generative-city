import maya.cmds as cmds
import sys 

def importMayaScript(nameFolder):

    myScriptDir = cmds.internalVar(userScriptDir=True)
    setScriptDir = myScriptDir+'generative-city/src/'+str(nameFolder)+'/'
    sys.path.append(setScriptDir)
    
importMayaScript("env")      
importMayaScript("element")      

from water import water
from Terrain_hexagon_gen import terrain

"""-----------Ne pas toucher les imports ----------------"""

cmds.file(f=True, new=True)


terrain()
water()


if __name__ == '__main__':
    terrain()
    water()

