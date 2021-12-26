import maya.cmds as cmds

cmds.file(f=True, new=True)


myScriptDir = cmds.internalVar(userScriptDir=True)
setMeshDir = myScriptDir+'generative-city/src/element/mesh/'

def openMayaFile(NameFile):
    # cmds.file( setMeshDir+NameFile, o=True )
    cmds.file( setMeshDir+NameFile, r=True)
    #cmds.file( setMeshDir+NameFile, r=True, type='mayaAscii', namespace='rubble' )

    # Query the setAttr edits:
    #cmds.reference( rfn='batiment_CyberPunk_uv', q=True, editCommand=True )

def openTextureFile(nameFile):
    filePath = str(setMeshDir) + str(nameFile)
    return(filePath)

openMayaFile("batiment_CyberPunk_uv.mb")

"""
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
"""