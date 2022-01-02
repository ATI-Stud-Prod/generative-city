#Curve 
cmds.curve( p=[(0, 2, 0), (3, 1, 6), (5, 3, 7), (9, 4, 9), (12, 5, 2)], k=[0,0,0,1,2,2,2] )

#cmds.polyCube(w = 1.641618, h= 0.197462, d=0.481802)

#pCube1 est le nom du mesh du pont
#selectionnez pour creer le pont
cmds.select('pCube1')
cmds.setAttr("pCube1.translateX", 0)
cmds.setAttr("pCube1.translateY", 0)
cmds.setAttr("pCube1.translateZ", 0)
pont = mapi.Network()

pont.createNetwork(name="pont", distributionStyle=7)

curveNode = pont.addNode("MASH_Curve")
pont_Mash_Dist = pont.distribute
cmds.connectAttr('curve1' + '.worldSpace[0]', 'pont_Curve' + ".inCurves[0]", force=1)
cmds.setAttr(curveNode.name+".timeStep", 1)
cmds.setAttr(pont_Mash_Dist+".pointCount", 44)

print pont.waiter
print pont.distribute
print pont.instancer

#WIP
# def curveSurterre():
#     choice = random.choice([True, False, False, False])
#     for cl in range (0,arrayZ*arrayX*2,1):
#         Hface = cmds.xform("pCylinder"+str(cl+1)+".f[13]",ws=True, q=True,t=True)
#         HfaceY = Hface[1]
#         cmds.select("pCylinder"+str(cl+1))
#         listPoint = []
#         listPoint.append(Hface)
#         if (choice) :

#             cmds.select( all=True )

#     p = cmds.xform("pPlane1.f[0]",ws=True, q=True,t=True)