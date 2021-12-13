import maya.cmds as cmds
import sys 

def importMayaScript(nameFolder):

    myScriptDir = cmds.internalVar(userScriptDir=True)
    setScriptDir = myScriptDir+'generative-city/src/'+str(nameFolder)+'/'
    
    #if(sys.path == "/generative-city/src/env/"):
    """
    pathExist = False;
    for i in range(len(sys.path)-1):
        
        if(sys.path[i] == setScriptDir):
            pathExist = True
            
    if(pathExist == True):
        print("test")
        sys.path.append(setScriptDir)
    """
    sys.path.append(setScriptDir)
    
importMayaScript("env")      
importMayaScript("element")      

from water import water
from Terrain_hexagon_gen import terrain

"""-----------Ne pas toucher les imports ----------------"""

cmds.file(f=True, new=True)


terrain()
water()

