import maya.cmds as cmds

#variable de terrain
arrayZ = 5
arrayX = 5

#Obtenir le shadingGrp et le shader de l'objet selectionne
#getshadingGrps[0] pour le shadingGrp
#getshadingGrps[1] pour le shader
def getShadingGrps():
    shapesInSel = cmds.ls(dag=1,o=1,s=1,sl=1)
    shadingGrps = cmds.listConnections(shapesInSel,type='shadingEngine')
    shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
    shadingGrps.append(''.join(shaders))
    return shadingGrps

#mettre des grilles sur les mesh terre
# objs les shader qui vont avoir la grille
def placementDeGrille(*objs):
    for x in range(0,arrayZ*arrayX*2,1):
        posH = cmds.xform("pCylinder"+str(x+1), ws=True, q=True, t=True)
        cmds.select("pCylinder"+str(x+1))
        if getShadingGrps()[1] in objs:
            cmds.polyPlane(w=1.5, h=1.5, sx=3, sy=3)
            #hauteur du vertex le plus haut de la tuile
            haut = cmds.xform("pCylinder"+str(x+1)+".vtx[12]", ws=True, q=True, t=True)
            cmds.move(posH[0], haut[1], posH[2])

#compter le nombre de plane et enlever les shapes
def countTerre():
    ls = cmds.ls('pPlane*')
    return sum(map(lambda x : "Shape" not in x , ls))

#mettre des objets sur les face des planes
def objFacePlacement(objs):
    for i in range(countTerre()):
        for j in range(9):
            p = cmds.xform("pPlane"+str(i+1)+".f["+str(j)+"]", ws=True, q=True, t=True)
            px = (p[0]+p[3]+p[6]+p[9]) * 0.25
            py = (p[1]+p[4]+p[7]+p[10]) * 0.25
            pz = (p[2]+p[5]+p[8]+p[11]) * 0.25

            objChoix = random.choice(objs)
            cmds.duplicate(objChoix)
            cmds.move(px, py, pz, objChoix)

#mettre des objets sur les vertices des planes
def objVerticePlacement(*objs):
    for i in range(countTerre()):
        for j in range(14):
            if j not in [0, 3, 15, 12]:
                p = cmds.xform("pPlane"+str(i+1)+".f["+str(j)+"]", ws=True, q=True,t=True)
                px = (p[0]+p[3]+p[6]+p[9]) * 0.25
                py = (p[1]+p[4]+p[7]+p[10]) * 0.25
                pz = (p[2]+p[5]+p[8]+p[11]) * 0.25

                objChoix = random.choice(objs)
                cmds.duplicate(objChoix)
                cmds.move(px, py, pz, objChoix)

#position des grilles
placementDeGrille('blinn7','blinn8','blinn9')

#positionnement des objets sur les faces
objFacePlacement(['bat1','bat2','bat3','bat4','bat5','bat6','bat7'])