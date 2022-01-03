import maya.cmds as cmds
import sys 

cmds.file(f=True, new=True)

def importMayaScript(nameFolder):

    myScriptDir = cmds.internalVar(userScriptDir=True)
    setScriptDir = myScriptDir+'generative-city/src/'+str(nameFolder)+'/'

    sys.path.append(setScriptDir)
    
importMayaScript("element")      
from uinterface import UI



def selectEdgeArround(theFace):
    vfList = cmds.polyListComponentConversion( theFace, ff=True, tvf=True )
    #print(vfList)
    vfList = cmds.ls( vfList, flatten=True )
    edgeArround =[]
    cmds.polySelect(theFace, r=True, add=True)
    for vf in vfList:
        edge = cmds.polyListComponentConversion( vf, fvf=True, te=True )
        cmds.select(edge, r=True, add=True)
    print(edgeArround)
    #cmds.select(edgeArround[1], r=True, add=True)

    #cmds.ls(edgeArround, flatten=True)


        
# ref : https://www.pinterest.fr/pin/93801604729453729/
""" @buildingType = [basic, elongated]"""

class Element:
    
    def __init__(self,mesh, hauteur, largeur,sub,pos=[0,0,0], buildingType="basic",  translateZ=0):
        self.mesh = mesh
        self.hauteur = hauteur
        self.largeur = largeur
        self.sub = sub
        self.pos = pos
        self.buildingType = buildingType
        self.translateZ = translateZ
    
    def selectSideFace(self, wallSubX):
        nbrFace = self.sub
        if (wallSubX != 0):
            nbrFace = (self.sub)*4**(wallSubX-1)
        return(nbrFace)
            
    def selectTopFace(self, wallSubX):
        nbrFace = self.sub
        if (wallSubX != 0):
            nbrFace = (self.sub*self.sub)*4**(wallSubX-1)
        return(nbrFace)

    def structureMesh(self,Pos=[0,0,0], Rotation=[0,0,0] , wallSubX=0, wallSubY=0 ):
        print(Pos)
        mesh = cmds.polyCylinder(name="generativeMesh", sx=self.sub,sy=1, sz=1, h=self.hauteur,radius=self.largeur)
        if (self.sub == 4 ):
            cmds.delete(mesh[0]+'.f[8:10]')
            cmds.delete(mesh[0]+'.f[4:8]')
            cmds.polyCloseBorder(ch=True)
            cmds.delete(mesh[0]+'.f[0:'+str((self.sub*2)-1)+']')
            cmds.select(mesh[0])
            #cmds.move(0,-self.hauteur*.5,0, moveXZ=False)
            cmds.rotate(0,'45deg',0)
            cmds.delete(mesh[0], constructionHistory = True)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            cmds.move(Pos[0], Pos[1], Pos[2])

        else:
            cmds.move(Pos[0], Pos[1], Pos[2])
            cmds.delete(mesh[0]+'.f[0:'+str((self.sub*2)-1)+']')
            cmds.delete(mesh[0], constructionHistory = True)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)


        
        cmds.rotate(''+str(Rotation[0])+'deg',''+str(Rotation[1])+'deg',''+str(Rotation[2])+'deg')
        cmds.polySubdivideFacet(dv=wallSubX)
        cmds.select(mesh[0]+'.f[0:*]')
        
        cmds.polyExtrudeFacet(kft=True, ltz=self.hauteur, divisions=wallSubY)
        cmds.delete(mesh[0], constructionHistory = True)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

        MeshValue = cmds.polyEvaluate()
        lastVertex = MeshValue['vertex'] -1
        lastEdge = MeshValue['edge'] -1
        lastFace = MeshValue['face'] -1
    
        if (self.sub == 4 ):
            selectTopFace = mesh[0]+'.f['+str(0)+':'+str(self.sub**wallSubX -1 )+']'
        else :    
            selectTopFace = mesh[0]+'.f['+str(0)+':'+str(self.selectTopFace(wallSubX) -1 )+']'
        
        selectSideFace = mesh[0]+'.f['+str(((lastFace-self.selectSideFace(wallSubX))+1))+':'+str(lastFace)+']'
            
        cmds.select(selectSideFace)
        """----  Param selection -----"""
        cmds.select(cl=True)
        
        self.mesh = {"meshName":mesh[0], "selectTopFace" :selectTopFace,"selectSideFace" : selectSideFace}
        return(self.mesh)

    def building(self, nbEtage):
        listforGroup = []
        createGroupe = cmds.group( em=True, name='building_'+str(self.buildingType) )
        for i in range(nbEtage):
            cmds.parent( self.floor(i, nbEtage),str(createGroupe) )
            
            cmds.move(self.pos[0],(self.pos[1]-(self.hauteur*.5+self.translateZ))+(i*(self.hauteur+self.translateZ)),self.pos[2])
        
    def elongated(self, offset, keepFacesTogether):
        cmds.polyExtrudeFacet(ltz=self.translateZ, d=1, off=offset, kft=keepFacesTogether)
    
    def floor(self, nbrFloor, lastFloor):
        mesh = self.structureMesh([self.pos[0],self.pos[1],self.pos[2]])
        if (self.buildingType == "elongated"):
                cmds.select(mesh["selectTopFace"])
                print("start elongated")
                
                self.elongated(1.5, True)
            
        else:
                cmds.select(mesh["selectTopFace"])
                cmds.polyBevel()
                
        if(nbrFloor != 0):
            print("beetwenn floor")
        elif(nbrFloor==lastFloor):
            print("last floor")
        else:
            print("firstFloor")
        
        """ A activer"""
        cmds.select(cl=True)
        cmds.select(self.mesh["meshName"])
        return(str(mesh["meshName"]))

if __name__ == '__main__':
    init = Element("generativeBat",1,3,4, [8,0,0],"basic")
    #init.structureMesh()
    #init.structureMesh([10,0,0],[0,0,0],0,0)
    init.building(8)
    