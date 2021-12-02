import maya.cmds as cmds
import random as random
cmds.file(f=True, new=True)
cpcurve = 0

#valeur à changer et mettre dans une fenetre
arrayZ = 30 #nombre sur l'axe des z
arrayX = 30 #nombre sur l'axe des x
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
        """cmds.softSelect(sse=False)"""

#creation des cylindres selon les lignes
for nb in range (0,arrayZ*arrayX,1) :
    cmds.softSelect(sse=False)
    for c in range (0,2,1) :
        posV = cmds.xform("curve"+str(nb+1)+".cv["+str(c)+"]", ws = True, q=True,t=True)
        posX = posV[0]
        posY = posV[1]
        posZ = posV[2]
        cmds.polyCylinder(sx=6)
        print "pCylinder"+str((c+1)+((nb)*2))
        #bevel des edges du dessus
        cmds.polyBevel("pCylinder"+str((c+1)+((nb)*2))+".e[7]","pCylinder"+str((c+1)+((nb)*2))+".e[8]","pCylinder"+str((c+1)+((nb)*2))+".e[9]","pCylinder"+str((c+1)+((nb)*2))+".e[10]","pCylinder"+str((c+1)+((nb)*2))+".e[11]","pCylinder"+str((c+1)+((nb)*2))+".e[6]",offset=0.1)
        cmds.scale(1.15,1.15,1.15)
        cmds.move(posX,posY,posZ)
cmds.select( all=True )