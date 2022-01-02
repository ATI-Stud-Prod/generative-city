import maya.cmds as cmds
import random as random
#valeur changer et mettre dans une fenetre
arrayZ = 20 #nombre sur l'axe des z
arrayX = 20 #nombre sur l'axe des x
        
def nuage():
    
    blanc = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr('blinn1.colorR',1)
    cmds.setAttr('blinn1.colorG',1)
    cmds.setAttr('blinn1.colorB',1)
    cmds.setAttr('blinn1.incandescence',1,1,1)
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
    cmds.connectAttr('blinn1.outColor','blinn1SG.surfaceShader')

    #creation des lignes 
    for cx in range (0,arrayX,1) :
        cmds.select( all=True )
        cmds.move(3.45,0,0, relative=True)
        cmds.select( clear=True )
        for cz in range (0,arrayZ,1) :
            cmds.curve( p=[(-0.862225, 0, -0.5), (0.862225, 0, 0.5)])
            cmds.move(0,0,cz*2)

    #creation du displacement
    crpas = random.randint(1,5)
    for cdis in range (0,arrayZ*arrayX,crpas) :  
        crpas = random.randint(1,5) 
        crpas2 = random.randint(1,2)
        for ca in range (0,2,crpas2) :
            fY = random.randint(0,2)
            cmds.select("curve"+str(cdis+1)+".cv["+str(ca)+"]")
            cmds.softSelect(sse=True)
            cmds.move(0,fY,0, relative=True)
            cmds.softSelect(sse=False)

    #creation des cylindres selon les lignes
    for cnb in range (0,arrayZ*arrayX,1) :
        for cc in range (0,2,1) :
            posV = cmds.xform("curve"+str(cnb+1)+".cv["+str(cc)+"]", ws = True, q=True,t=True)
            posX = posV[0]
            posY = posV[1]
            posZ = posV[2]
            cmds.polyCylinder(sx=6, h=0.7, name="nNuage"+str((cc+1)+((cnb)*2)))
            cmds.sets(edit=True, forceElement= 'blinn1SG') 
            #bevel des edges du dessus
            cmds.polyBevel("nNuage"+str((cc+1)+((cnb)*2))+".e[7]","nNuage"+str((cc+1)+((cnb)*2))+".e[8]","nNuage"+str((cc+1)+((cnb)*2))+".e[9]","nNuage"+str((cc+1)+((cnb)*2))+".e[10]","nNuage"+str((cc+1)+((cnb)*2))+".e[11]","nNuage"+str((cc+1)+((cnb)*2))+".e[6]",offset=0.1)
            #bevel des edges du dessus
            cmds.polyBevel("nNuage"+str((cc+1)+((cnb)*2))+".e[0]","nNuage"+str((cc+1)+((cnb)*2))+".e[1]","nNuage"+str((cc+1)+((cnb)*2))+".e[2]","nNuage"+str((cc+1)+((cnb)*2))+".e[3]","nNuage"+str((cc+1)+((cnb)*2))+".e[4]","nNuage"+str((cc+1)+((cnb)*2))+".e[5]",offset=0.1)
            cmds.scale(1.15,1.15,1.15)
            cmds.move(posX,posY,posZ)
    #on monte tout au dessus
    for cloud in range (0,arrayZ*arrayX*2,1):
        cmds.select("nNuage"+str(cloud+1))
        cmds.move(0,9,0,relative=True)
    #assignement des couleurs selon la hauteur
    for cl in range (0,arrayZ*arrayX*2,1): 
        Hface = cmds.xform("nNuage"+str(cl+1)+".f[13]",ws=True, q=True,t=True)
        HfaceY = Hface[1]
        cmds.select("nNuage"+str(cl+1))
        if (HfaceY <=10.6) :
            cmds.delete()
    #Delete des curves 
    for dl in range (0,arrayZ*arrayX,1):
        cmds.select("curve"+str(dl+1))
        cmds.delete()
        
    cmds.select( all=True )

cmds.file(f=True, new=True)
nuage()
