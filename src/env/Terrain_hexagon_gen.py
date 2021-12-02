import maya.cmds as cmds
import random as random
cmds.file(f=True, new=True)

arrayZ = 10
arrayX = 10
cpcurve = 0

for x in range (0,arrayX,1) :
    cmds.select( all=True )
    cmds.move(3.45,0,0, relative=True)
    cmds.select( clear=True )
    for z in range (0,arrayZ,1) :
        cmds.curve( p=[(-0.862225, 0, -0.5), (0.862225, 0, 0.5)])
        cmds.move(0,0,z*2)
        for c in range (0,2,1) :
            Rhigh = random.uniform(0,1)
            Rhigh2 = random.uniform(0,1)
            posV = cmds.xform("curve"+str((z+1)+cpcurve)+".cv["+str(c)+"]", ws = True, q=True,t=True)
            print "curve"+str((z+1)+cpcurve)
            posX = posV[0]
            posY = posV[1]
            posZ = posV[2]
            cmds.polyCylinder(sx=6)
            cmds.scale(1.15,1.15,1.15)
            cmds.move(posX,posY+Rhigh+Rhigh2,posZ)
    cpcurve = cpcurve+arrayX
cmds.select( all=True )