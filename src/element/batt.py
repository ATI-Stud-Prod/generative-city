import maya.cmds as cmds

cmds.file(f=True, new=True)



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
class Element:
    def __init__(self, hauteur, largeur,sub, typeTexture='null'):
        self.hauteur = hauteur
        self.largeur = largeur
        self.sub = sub
        self.typeTexture = typeTexture

    def building(self, nbEtage):
        for i in range(nbEtage):
            self.floor()
            cmds.move(0,(i)*self.hauteur,0, moveXZ=False)
        
    
    def floor(self):
        print("start create floor")
        mesh = cmds.polyCylinder(name="baseMesh", sx=self.sub,sy=1, sz=1, h=self.hauteur,radius=self.largeur)

        """ Set up of our variable and base mesh """
        if (self.sub == 4 ):
            cmds.delete(mesh[0]+'.f[8:10]')
            cmds.delete(mesh[0]+'.f[4:8]')
            cmds.rotate(0, '45deg',0)
            cmds.move(0,self.hauteur*.5,0)
            cmds.polyCloseBorder(ch=True)
            cmds.delete(mesh[0], constructionHistory = True)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)

            MeshValue = cmds.polyEvaluate()
            lastVertex = int((MeshValue['vertex'] /2) -1)
            lastEdge = int((MeshValue['edge'] /2) -1)
            lastFace = int((MeshValue['face'] /2) -1)
            
            selectTopFace = mesh[0]+'.f['+str(lastFace)+']'
            # Start mode 
            cmds.polyBevel(mesh[0]+'.f['+str(lastFace)+']',segments=1, autoFit=False )


        else:
            cmds.move(0,self.hauteur*.5,0)
            cmds.delete(mesh[0], constructionHistory = True)
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
            MeshValue = cmds.polyEvaluate()
            lastVertex = MeshValue['vertex'] -1
            lastEdge = MeshValue['edge'] -1
            lastFace = MeshValue['face'] -1
           
            selectTopFace = mesh[0]+'.f['+str(lastFace-self.sub+1)+':'+str(lastFace)+']'

            # Start mode           
            cmds.polySelect(edgeLoop=[5])
            #cmds.polySelect(edgeLoop=[1], add=True)
            cmds.polyBevel(segments=1, autoFit=False)
            # cmds.polySplit(constructionHistory=True, smoothingangle=[180],edgepoint=[5, .5,[baseMesh,baseMeshShape])
            
            # cmds.hilite(loopSelection[0],loopSelection[1])
            # cmds.polySplit()

        
         
   
        #selectEdgeArround(selectTopFace)
        """
        cmds.polyExtrudeFacet(mesh[0]+'.f['+str(lastFace)+']', kft=False, ltz=2)
        cmds.select(mesh[0]+'.f['+str(lastFace)+']', tgl=True)
        """

        #cmds.polyExtrudeFacet(mesh+'.f['+str(lastFace)+']', kft=False, ltz=2)
        #print(lastEdge)
        
        
        #cut1 = cmds.polyCut(cd='x', ef=0, ch=1 )
        #cmds.select(mesh[0]+'.e['+str(lastEdge+self.sub)+':'+str(lastEdge+(self.sub)*2)+']')
        
        #cmds.select( cut1, tgl=True )
        #cmds.polyBevel(mesh[0]+'.e['+str(lastEdge+1)+":"+str(lastEdge+self.sub)+']',segments=4, autoFit=False )

        # cmds.select(test)
        
        #cmds.polyCut(cd='Z', ef=0, ch=1 )
        
        cmds.select(cl=True)
        cmds.select(mesh[0])

if __name__ == '__main__':
    init = Element(3,5,5)
    init.building(12)