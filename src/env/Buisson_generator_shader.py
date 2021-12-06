#---------------------------------------------------------------#

# tp 5 : Shader Generator
#Créer un script qui génere des shaders aléatoire (couleurs, textures...)
#Option : vous pouvez créer une petite interface qui permet de les générer, et de les assigner à vos objets.

#-------------------------------------------------------------#

import math
import maya.cmds as cmds
import random as random
import mtoa.utils as mutils
cmds.file(f=True,new=True)

#-----------------------------------------------------

def Scene():
    
    cmds.file(f=True,new=True)
    
    
# Pour le rendu

mutils.createLocator("aiSkyDomeLight", asLight=True)
panel = cmds.getPanel(wf=1)
cmds.modelEditor(panel, e=1, allObjects=0)
cmds.modelEditor(panel, e=1, polymeshes=1) 
cmds.modelEditor(panel, e=1, displayTextures=1)

# A-Création d'un shader et application du shader de base

b = cmds.shadingNode('blinn', asShader=True)
cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
cmds.connectAttr('blinn1.outColor', 'blinn1SG.surfaceShader')

h= 10
rayon = 1

mini = 20
maxi = 40

r = math.ceil(random.uniform(mini,maxi))


print(r)
for s in range(int(r)):
    sphereName = cmds.polySphere()
    sphereName = "pSphere"+str(s+1)
    posX = random.uniform(-10, 10)
    posY = random.uniform(0, 0)
    posZ = random.uniform(-10, 10)
    cmds.move(posX/rayon,2/rayon-1, posZ/rayon)
    
    nbf = cmds.polyEvaluate(face=True)
    print(nbf)
    cmds.sets(edit=True, forceElement = 'blinn1SG')
  
  
# a- Déformation aléatoir du scale à partir d'un random basé sur les faces des pierres sélectionné avec un pas de 7

    min = 0.950
    max = 1.015
    randomX = random.uniform(min, max)
    randomY = random.uniform(min, max)
    randomZ = random.uniform(min, max)
         
    for i in range(0, nbf,7):
     
         cmds.select(sphereName+".f["+str(i)+"]", add=True)
         cmds.scale(randomX,randomY,randomZ)       

    cmds.select(clear = True)
    cmds.select(sphereName)


#Ajouter une texture de noise

cmds.shadingNode('noise', asTexture=True)
cmds.shadingNode('place2dTexture', asUtility=True)
cmds.connectAttr( 'place2dTexture1.outUV', 'noise1.uvCoord')
cmds.connectAttr('noise1.outAlpha', 'blinn1.diffuse')

#-------------------------------------------------------------------------

# Creation d'une interface

cmds.window(title= "Générateur des Shaders",widthHeight=(395, 232))

#Choix d'un style de fenetre

cmds.columnLayout()
cmds.text("Création d'un Shader")



# Une fonction qui cree et applique un shader blinn

def blinnFunction():
    myShader = cmds.shadingNode('blinn', asShader=True)
    mySGBlinn = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=myShader+'SG')
    cmds.connectAttr(myShader+'.outColor', mySGBlinn+'.surfaceShader')
    cmds.select('pSphere1')
    cmds.sets(edit=True, forceElement=myShader+'SG')

# Un bouton pour créer un autre Shader blinn

cmds.button(h=30, w=50, label="blinn", c="blinnFunction()", backgroundColor=[1,1,1])

cmds.text("Choix couleur Blinn")


# Un slider pour choisir les couleurs du blinn

slider1 = cmds.floatSliderGrp(min =0.0,max=1.0,label="BlinnRed", field= True, backgroundColor=[1,0,0])
slider2 = cmds.floatSliderGrp(min =0.0,max=1.0,label="BlinnGreen", field= True, backgroundColor=[0,1,0])
slider3 = cmds.floatSliderGrp(min =0.0,max=1.0,label="BlinnBlue", field= True, backgroundColor=[0,0,1])


# Une fonction qui change la couleur d'un shader blinn

def changerColor():
    v1=cmds.floatSliderGrp(slider1, q= True,v=True)
    v2=cmds.floatSliderGrp(slider2, q= True,v=True)
    v3=cmds.floatSliderGrp(slider3, q= True,v=True)
    cmds.select('pSphere1')
    cmds.setAttr('blinn1.colorR',v1)
    cmds.setAttr('blinn1.colorG',v2)
    cmds.setAttr('blinn1.colorB',v3)
    
# Un bouton pour appliquer la couleur pour un Shader blinn

cmds.text("Appliquer la couleur couleur")
cmds.button(h=30, w=70,label="blinnColor", c="changerColor()",backgroundColor=[250,250,250])

# Un bouton pour refresh la scène

cmds.text("Nettoyer la scene")
Refresh = cmds.button( h = 50, l = "Refresh", command = "Scene()")

# Affichage de la fenetre

cmds.showWindow()
