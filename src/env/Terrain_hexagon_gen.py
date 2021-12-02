import maya.cmds as cmds
import random as random
cmds.file(f=True, new=True)

arrayZ = 10
arrayX = 5
cpcurve = 0
min = 0
max = 1

for x in range (0,arrayX,1) :
    cmds.select( all=True )
    cmds.move(3.45,0,0, relative=True)
    cmds.select( clear=True )
    for z in range (0,arrayZ,1) :
        cmds.curve( p=[(-0.862225, 0, -0.5), (0.862225, 0, 0.5)])
        cmds.move(0,0,z*2)
        cpcurve = cpcurve+arrayX

rpas = random.randint(1,5)
for dis in range (0,arrayZ*arrayX,rpas) :
    for a in range (0,2,1) :
        fY = random.randint(min,max)
        cmds.select("curve"+str(dis+1)+".cv["+str(a)+"]")
        cmds.move(0,fY,0, relative=True)


for nb in range (0,arrayZ*arrayX,1) :
    for c in range (0,2,1) :
        posV = cmds.xform("curve"+str(nb+1)+".cv["+str(c)+"]", ws = True, q=True,t=True)
        posX = posV[0]
        posY = posV[1]
        posZ = posV[2]
        cmds.polyCylinder(sx=6)
        cmds.scale(1.15,1.15,1.15)
        cmds.move(posX,posY,posZ)
cmds.select( all=True )