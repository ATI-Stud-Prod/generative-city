import maya.cmds as cmds
import random as random

#valeur changer et mettre dans une fenetre

arrayZ = 20 #nombre sur l'axe des z
arrayX = 20 #nombre sur l'axe des x
min = 0 #minumim du displacement
max = 1 #maximum du displacement
        
#creation des shaders
def terrain():
    #green
    green1 = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr('blinn1.colorR',0.1)
    cmds.setAttr('blinn1.colorG',0.6)
    cmds.setAttr('blinn1.colorB',0)
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
    cmds.connectAttr('blinn1.outColor','blinn1SG.surfaceShader')

    green2 = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr('blinn2.colorR',0)
    cmds.setAttr('blinn2.colorG',0.6)
    cmds.setAttr('blinn2.colorB',0)
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
    cmds.connectAttr('blinn2.outColor','blinn1SG1.surfaceShader')

    green3 = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr('blinn3.colorR',0)
    cmds.setAttr('blinn3.colorG',0.6)
    cmds.setAttr('blinn3.colorB',0.1)
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
    cmds.connectAttr('blinn3.outColor','blinn1SG2.surfaceShader')

    #blue
    blue1 = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr('blinn4.colorR',0)
    cmds.setAttr('blinn4.colorG',0.3)
    cmds.setAttr('blinn4.colorB',0.6)
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
    cmds.connectAttr('blinn4.outColor','blinn1SG3.surfaceShader')

    blue2 = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr('blinn5.colorR',0)
    cmds.setAttr('blinn5.colorG',0.4)
    cmds.setAttr('blinn5.colorB',0.6)
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
    cmds.connectAttr('blinn5.outColor','blinn1SG4.surfaceShader')

    blue3 = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr('blinn6.colorR',0)
    cmds.setAttr('blinn6.colorG',0.5)
    cmds.setAttr('blinn6.colorB',0.6)
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
    cmds.connectAttr('blinn6.outColor','blinn1SG5.surfaceShader')

    #beige
    beige1 = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr('blinn7.colorR',0.9)
    cmds.setAttr('blinn7.colorG',0.5)
    cmds.setAttr('blinn7.colorB',0.4)
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
    cmds.connectAttr('blinn7.outColor','blinn1SG6.surfaceShader')

    beige2 = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr('blinn8.colorR',0.9)
    cmds.setAttr('blinn8.colorG',0.6)
    cmds.setAttr('blinn8.colorB',0.4)
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
    cmds.connectAttr('blinn8.outColor','blinn1SG7.surfaceShader')

    biege3 = cmds.shadingNode('blinn', asShader=True)
    cmds.setAttr('blinn9.colorR',0.9)
    cmds.setAttr('blinn9.colorG',0.7)
    cmds.setAttr('blinn9.colorB',0.4)
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='blinn1SG')
    cmds.connectAttr('blinn9.outColor','blinn1SG8.surfaceShader')

    #creation des fonctions pour assigner les shaders

    #green
    def cgreen1() :
        cmds.sets(edit=True, forceElement= 'blinn1SG')    
    def cgreen2() :
        cmds.sets(edit=True, forceElement= 'blinn1SG1')
    def cgreen3() :
        cmds.sets(edit=True, forceElement= 'blinn1SG2')
    def greencolor() :
        my_list = [(cgreen1),(cgreen2),(cgreen3)]
        my_samp = 1
        numColor = random.sample(my_list,my_samp)
        numColor[0]()

    #blue
    def cblue1() :
        cmds.sets(edit=True, forceElement= 'blinn1SG3')    
    def cblue2() :
        cmds.sets(edit=True, forceElement= 'blinn1SG4')
    def cblue3() :
        cmds.sets(edit=True, forceElement= 'blinn1SG5')
    def bluecolor() :
        my_list = [(cblue1),(cblue2),(cblue3)]
        my_samp2 = 1
        numColor2 = random.sample(my_list,my_samp2)
        numColor2[0]()
        
    #beige
    def cbeige1() :
        cmds.sets(edit=True, forceElement= 'blinn1SG6')    
    def cbeige2() :
        cmds.sets(edit=True, forceElement= 'blinn1SG7')
    def cbeige3() :
        cmds.sets(edit=True, forceElement= 'blinn1SG8')
    def beigecolor() :
        my_list = [(cbeige1),(cbeige2),(cbeige3)]
        my_samp3 = 1
        numColor3 = random.sample(my_list,my_samp3)
        numColor3[0]()

    #creation des lignes 
    for x in range (0,arrayX,1) :
        cmds.select( all=True )
        cmds.move(3.45,0,0, relative=True)
        cmds.select( clear=True )
        for z in range (0,arrayZ,1) :
            cmds.curve( p=[(-0.862225, 0, -0.5), (0.862225, 0, 0.5)])
            cmds.move(0,0,z*2)

    #creation du displacement
    rpas = random.randint(1,5)
    for dis in range (0,arrayZ*arrayX,rpas) :  
        rpas = random.randint(1,5) 
        rpas2 = random.randint(1,2)
        for a in range (0,2,rpas2) :
            fY = random.randint(min,max)
            cmds.select("curve"+str(dis+1)+".cv["+str(a)+"]")
            cmds.softSelect(sse=True)
            cmds.move(0,fY,0, relative=True)
            cmds.softSelect(sse=False)

    #creation des cylindres selon les lignes
    for nb in range (0,arrayZ*arrayX,1) :
        for c in range (0,2,1) :
            posV = cmds.xform("curve"+str(nb+1)+".cv["+str(c)+"]", ws = True, q=True,t=True)
            posX = posV[0]
            posY = posV[1]
            posZ = posV[2]
            cmds.polyCylinder(sx=6)
            #bevel des edges du dessus
            cmds.polyBevel("pCylinder"+str((c+1)+((nb)*2))+".e[7]","pCylinder"+str((c+1)+((nb)*2))+".e[8]","pCylinder"+str((c+1)+((nb)*2))+".e[9]","pCylinder"+str((c+1)+((nb)*2))+".e[10]","pCylinder"+str((c+1)+((nb)*2))+".e[11]","pCylinder"+str((c+1)+((nb)*2))+".e[6]",offset=0.1)
            cmds.scale(1.15,1.15,1.15)
            cmds.move(posX,posY,posZ)

    #assignement des couleurs selon la hauteur
    for cl in range (0,arrayZ*arrayX*2,1): 
        Hface = cmds.xform("pCylinder"+str(cl+1)+".f[13]",ws=True, q=True,t=True)
        HfaceY = Hface[1]
        cmds.select("pCylinder"+str(cl+1))
        beigecolor()
        if (HfaceY <= 2) :
            bluecolor()
        elif (HfaceY >= 2.5) :
            greencolor()
    cmds.select( all=True )

