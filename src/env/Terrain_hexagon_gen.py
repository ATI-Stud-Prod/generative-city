import maya.cmds as cmds
import random as random
cmds.file(f=True, new=True)
cpcurve = 0

#valeur à changer et mettre dans une fenetre
arrayZ = 10 #nombre sur l'axe des z
arrayX = 6 #nombre sur l'axe des x
min = 0 #minumim du displacement
max = 1 #maximum du displacement

#creation des lignes 
for x in range (0,arrayX,1) :
    cmds.select( all=True )
    cmds.move(3.45,0,0, relative=True)
    cmds.select( clear=True )
    for z in range (0,arrayZ,1) :
        cmds.curve( p=[(-0.862225, 0, -0.5), (0.862225, 0, 0.5)])
        cmds.move(0,0,z*2)
        cpcurve = cpcurve+arrayX

#creation du displacement
rpas = random.randint(1,5)
for dis in range (0,arrayZ*arrayX,rpas) :    
    for a in range (0,2,1) :
        fY = random.randint(min,max)
        cmds.select("curve"+str(dis+1)+".cv["+str(a)+"]")
        cmds.softSelect(sse=True)
        cmds.move(0,fY,0, relative=True)
        cmds.softSelect(sse=False)
        
#creation des shaders
myShader1 = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr('blinn1.colorR',1)
cmds.setAttr('blinn1.colorG',0)
cmds.setAttr('blinn1.colorB',0)
cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
cmds.connectAttr('blinn1.outColor','blinn1SG.surfaceShader')

myShader2 = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr('blinn2.colorR',0)
cmds.setAttr('blinn2.colorG',1)
cmds.setAttr('blinn2.colorB',0)
cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
cmds.connectAttr('blinn2.outColor','blinn1SG1.surfaceShader')

myShader3 = cmds.shadingNode('blinn', asShader=True)
cmds.setAttr('blinn3.colorR',0)
cmds.setAttr('blinn3.colorG',0)
cmds.setAttr('blinn3.colorB',1)
cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
cmds.connectAttr('blinn3.outColor','blinn1SG2.surfaceShader')

#creation des fonctions pour assigner les shaders random
def blcolor1() :
    cmds.sets(edit=True, forceElement= 'blinn1SG')    

def blcolor2() :
    cmds.sets(edit=True, forceElement= 'blinn1SG1')

def blcolor3() :
    cmds.sets(edit=True, forceElement= 'blinn1SG2')

#creation des cylindres selon les lignes
for nb in range (0,arrayZ*arrayX,1) :
    for c in range (0,2,1) :
        posV = cmds.xform("curve"+str(nb+1)+".cv["+str(c)+"]", ws = True, q=True,t=True)
        posX = posV[0]
        posY = posV[1]
        posZ = posV[2]
        cmds.polyCylinder(sx=6)
        #assigne des shaders random
        my_list = [(blcolor1),(blcolor2),(blcolor3)]
        my_samp = 1
        numColor = random.sample(my_list,my_samp)
        numColor[0]()
        #bevel des edges du dessus
        cmds.polyBevel("pCylinder"+str((c+1)+((nb)*2))+".e[7]","pCylinder"+str((c+1)+((nb)*2))+".e[8]","pCylinder"+str((c+1)+((nb)*2))+".e[9]","pCylinder"+str((c+1)+((nb)*2))+".e[10]","pCylinder"+str((c+1)+((nb)*2))+".e[11]","pCylinder"+str((c+1)+((nb)*2))+".e[6]",offset=0.1)
        cmds.scale(1.15,1.15,1.15)
        cmds.move(posX,posY,posZ)
cmds.select( all=True )