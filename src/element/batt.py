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
    #self.mesh = cmds.polyCylinder(name="baseMesh", sx=self.sub,sy=1, sz=1, h=self.hauteur,radius=self.largeur)

    
    def __init__(self, hauteur, largeur,sub, buildingType="basic",  translateZ=0, typeTexture='null'):
        self.hauteur = hauteur
        self.largeur = largeur
        self.buildingType = buildingType
        self.sub = sub
        
        self.typeTexture = typeTexture
        
        self.translateZ = translateZ 


    def structureMesh(self,PosX, PosY, PosZ, Rotation=0 , wallSubX=0,wallSubY=0 ):
        mesh = cmds.polyCylinder(name="baseMesh", sx=self.sub,sy=1, sz=1, h=self.hauteur,radius=self.largeur)
        if (self.sub == 4 ):
            cmds.delete(mesh[0]+'.f[8:10]')
            cmds.delete(mesh[0]+'.f[4:8]')
            cmds.polyCloseBorder(ch=True)
            
            
            cmds.delete(mesh[0]+'.f[0:'+str((self.sub*2)-1)+']')
            cmds.select(mesh[0])
            cmds.move(0,-self.hauteur*.5,0, moveXZ=False)
            cmds.rotate(0,'45deg',0)
            cmds.delete(mesh[0], constructionHistory = True)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            
            
        else:
            cmds.move(PosX, PosY-self.hauteur*.5, PosZ)
            cmds.delete(mesh[0]+'.f[0:'+str((self.sub*2)-1)+']')
        

        cmds.rotate(0,''+str(Rotation)+'deg',0)
        cmds.polySubdivideFacet(dv=wallSubX)
        cmds.select(mesh[0]+'.f[0:*]')
        cmds.polyExtrudeFacet(kft=True, ltz=self.hauteur, divisions=wallSubY)
        cmds.delete(mesh[0], constructionHistory = True)
        cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

        MeshValue = cmds.polyEvaluate()
        lastVertex = MeshValue['vertex'] -1
        lastEdge = MeshValue['edge'] -1
        lastFace = MeshValue['face'] -1
           
        selectTopFace = mesh[0]+'.f['+str(lastFace-self.sub+1)+':'+str(lastFace)+']'
        DataMesh = {"meshName":mesh[0], "lastVertex":lastVertex, "lastEdge":lastEdge, "lastEdge": lastFace, "selectTopFace" : selectTopFace}
        
        return(DataMesh)

    def building(self, nbEtage):
        createGroupe = cmds.group( em=True, name='building_'+str(self.buildingType) )
        listforGroup = []
        for i in range(nbEtage):
            self.floor()
            cmds.move(0,(i)*(self.hauteur+self.translateZ),0, moveXZ=False)
    
    def elongated(self, division, offset, keepFacesTogether):
        cmds.polyExtrudeFacet(ltz=self.translateZ, d=division, off=offset, kft=keepFacesTogether)
    
    def floor(self):
        print("start create floor")

        mesh = self.structureMesh(1,1,1)
        if (self.buildingType == "elongated"):
            cmds.select(selectTopFace)
            self.elongated(3,1.5, True)
            cmds.polyBevel()
            #cmds.polyExtrudeFacet(kft=False, ltz=2)
            #cmds.select(mesh[0]+'.f['+str(lastFace)+']', tgl=True)
        else:
            cmds.polyBevel()
        
        """ A activer"""
        cmds.select(cl=True)
        cmds.select(mesh["meshName"])
        
    
    
    def Test(self):
        test= self.structureMesh(1,1,1)
        print(test)
    

if __name__ == '__main__':
    
    """---INTERFACE---"""
    """ 
    ui = UI('interface',300, 200)
    ui.make_btn(label='buton')
    ui.make_i_SliderGrp()
    """
    """---Build---"""
    init = Element(3,5,4, "basic")
    init.building(10)
    #init.structureMesh(0,0,0)
    #init.Test()

    