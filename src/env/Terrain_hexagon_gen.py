import maya.cmds as cmds
import random as random



def terrain(arrayZ,arrayX, min, max):
    #creation des lignes 
    for x in range (0,arrayX,1) :
        cmds.select( all=True )
        cmds.move(3.45,0,0, relative=True)
        cmds.select( clear=True )
        for z in range (0,arrayZ,1) :
            cmds.curve( p=[(-0.862225, 0, -0.5), (0.862225, 0, 0.5)])
            cmds.move(0,0,z*2)

    #creation du displacement
    rpas = random.randint(1,3)
    for dis in range(0,arrayZ*arrayX,rpas):  
        rpas = random.randint(1,3) 
        rpas2 = random.randint(1,2)
        for a in range (0,2,rpas2) :
            fY = random.randint(min,max)
            cmds.select("curve"+str(dis+1)+".cv["+str(a)+"]")
            cmds.softSelect(sse=True)
            cmds.move(0,fY,0, relative=True)
            cmds.softSelect(sse=False)

    #creation des cylindres selon les lignes
    for nb in range (0,arrayZ*arrayX,1):
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
    for cl in range(0,arrayZ*arrayX*2,1): 
        Hface = cmds.xform("pCylinder"+str(cl+1)+".f[13]",ws=True, q=True,t=True)
        HfaceY = Hface[1]
        cmds.select("pCylinder"+str(cl+1))
        rndBitume = randomColor([bitume1, bitume2, bitume3])
        shaderAssign(rndBitume)
        if HfaceY <= 2:
            rndBleu = randomColor([bleu1, bleu2, bleu3])
            shaderAssign(rndBleu)
        elif HfaceY >= 2.5:
            rndVert = randomColor([vert1, vert2])
            shaderAssign(rndVert)

def createShader(material, rgb, name):
    cmds.shadingNode(material, name= name, asShader=True, shared=True)
    cmds.setAttr(name+'.color',rgb[0], rgb[1], rgb[2], type= 'double3')
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=name+'SG')
    cmds.connectAttr(name+'.outColor',name+'SG.surfaceShader')
    return name

def shaderAssign(name):
    cmds.sets(edit=True, forceElement= "".join(name)+'SG')

def randomColor(liste_de_shader):
    return random.sample(liste_de_shader, 1)
