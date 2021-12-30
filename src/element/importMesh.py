import maya.cmds as cmds

cmds.file(f=True, new=True)


myScriptDir = cmds.internalVar(userScriptDir=True)
setMeshDir = myScriptDir+'generative-city/src/element/mesh/'


class ManageImport:
    
    def __init__(self,NameFile,path="" ,SelectedObj="", referenceName=""):
        self.NameFile = NameFile
        self.path = path
        self.SelectedObj = SelectedObj
        self.referenceName = referenceName
        
    def openMayaFile(self,referenceName="" ):
        if(referenceName != ""):
             Mayafile = cmds.file( self.path, removeReference=True)
             self.NameFile = referenceName
        
        self.path= setMeshDir+self.NameFile
        Mayafile = cmds.file( self.path, r=True, lockFile=False)
        nameFile = cmds.referenceQuery( self.path,  nodes=True  ) # bad
        self.SelectedObj = nameFile[0]
        self.referenceName = cmds.referenceQuery(self.path, filename = True)

        
    def deleteReference(self, nameReference=""):
        cmds.file( self.path, removeReference=True)
    
    def ManageObj(self,_pos=[0,0,0], _scale=[1,1,1], _rotation=["0deg","0deg","0deg"]):
        obj = self.SelectedObj
        cmds.select(obj)
        cmds.move(_pos[0],_pos[1],_pos[2])
        cmds.scale(_scale[0],_scale[1], _scale[2])
        cmds.rotate(str(_rotation[0])+"deg",str(_rotation[1])+"deg",str(_rotation[2])+"deg")
        return(obj)
        
    
if __name__ == '__main__':
    
    
    bilelBat = ManageImport("batiment_CyberPunk_uv.mb")
    bilelBat.openMayaFile()
    
    bilelBat.ManageObj([2,0,0],[1,1,1], [0,0,0])
    
    """ Si vous voulez changer après coup la reference vous pouvez spécifier un autre fichier """
    # bilelBat.openMayaFile("batiment_CyberPunk_avant_combine.mb")
    """ Si vous voulez delete """
    # bilelBat.deleteReference()

"""------------- Texture part ---------------"""

def openTextureFile(nameFile):
    filePath = str(setMeshDir) + str(nameFile)
    return(filePath)


#deleteMayaFile("batiment_CyberPunk_uv")

b = cmds.shadingNode('lambert', asShader=True)
cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='lambert1SG')
cmds.connectAttr('lambert1.outColor', 'lambert1SG.surfaceShader')

#ajout texture


cmds.shadingNode("file", asTexture=True)
cmds.shadingNode('place2dTexture', asUtility=True)
cmds.connectAttr( 'place2dTexture1.outUV', 'file1.uvCoord')
cmds.connectAttr('file1.outColor', 'lambert1.color')
cmds.setAttr( 'file'+ '1' +'.fileTextureName', openTextureFile("texture_texte_ati/building_mode_lambert4_Emissive.1002.png"), type = "string")

# Creation objet

Objet = cmds.polyCube(name = "objet"+str(1))
cmds.sets(edit=True, forceElement = 'lambert1SG')
