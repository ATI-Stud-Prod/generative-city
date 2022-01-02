import maya.cmds as cmds


#variable de terrain
arrayZ = 20
arrayX = 20

vtxDefaut = { "interdit_defaut" : [0,1,2,3,3,4,5,7,8,9,10,25,26,27,28,39,40,41,42,53,54,55,56,67,68,69,70,71,81,82,83,84] }

#nom du shader ou shaderGrp comme clef
tuiles = { "terreBitume" : [16,17,18,12,51,52,54,53,58,59,60,15,25,26,27,43,35,32],
           "terreBitume2" : [60,6,36,52,41,44,17,25,14],
           "terreBitume3" : [11,18,14,27,23,36,32,45,41,54,50,60],
           "terreBitume4" : [60,6,36,45,18,27,54],
           "terreBitume5" : [18,6,45,54,42,33,36,27,15,12,60],
           "terreBitume6" : [17,14,25,58,50,53,43,32,35]
                    }

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
# shader_list les shader qui vont avoir la grille
def placementDeGrille(shader_list=[]):
    for x in range(0,arrayZ*arrayX*2,1):
        #tuile position
        pos_h = cmds.xform("pCylinder"+str(x+1), ws=True, q=True, t=True)
        #selection de tuile
        cmds.select("pCylinder"+str(x+1))
        #verifier element en commun des deux listes
        shader_name = any(item in getShadingGrps() for item in shader_list)
        print(shader_name)
        print(getShadingGrps())
        if shader_name:
            cmds.polyDisc(sides=6,subdivisionMode=1,subdivisions=5)
            #hauteur du vertex le plus haut de la tuile
            haut = cmds.xform("pCylinder"+str(x+1)+".vtx[12]", ws=True, q=True, t=True)
            cmds.move(pos_h[0], haut[1], pos_h[2])

#compter le nombre de plane et enlever les shapes
def grilleCounter():
    ls = cmds.ls("pDisc*")
    return sum(map(lambda x : "Shape" not in x , ls))

#mettre des objets sur les vertices des planes
def objVerticePosition(tuiles_dict, objs):
    #choix d'une tuile
    tuile_vtx_interdit = random.sample(tuiles_dict, 1)
    for i in range(grilleCounter()):
        cmds.select("pCylinder"+str(i))
        for j in range(91):
            if j not in vtxDefaut["interdit_defaut"]:
                if "pDisc("+i+").vtx["+str(j)+"]" not in tuile_vtx_interdit:
                    objChoix = random.choice(objs)
                    cmds.duplicate(objChoix)
                    p = cmds.xform("pDisc"+str(i+1)+".vtx["+str(j)+"]", ws=True, q=True, t=True)
                    cmds.move(p[0], p[1], p[2], objChoix)

def objVerticePositionAvecTexture(tuiles_list, objs):
    sgName = getShadingGrps()[0] in tuiles_list.keys()
    sName = getShadingGrps()[1] in tuiles.keys()
    for i in range(grilleCounter()):
        if sgName or sName:
            for j in range(91):
                if j not in vtxDefaut["interdit_defaut"]:
                    vtx = "pDisc("+str(i+1)+").vtx["+str(j)+"]"
                    if vtx in tuiles[sName] or vtx in tuiles[sgName]:
                        objChoix = random.choice(objs)
                        cmds.duplicate(objChoix)
                        p = cmds.xform("pDisc"+str(i+1)+".vtx["+str(j)+"]", ws=True, q=True, t=True)
                        cmds.move(p[0], p[1], objChoix)

def deleteGrilles():
    ls = cmds.select(cmds.ls("pDisc*"))
    cmds.delete(ls)

#position des grilles
#placementDeGrille(['terreBitume','terreBitume2','terreBitume3'])

#positionnement des objets sur les faces
#objVerticePosition(['bat1','bat2','bat3','bat4','bat5','bat6','bat7'])

#objVerticePosition(tuiles, [cmds.polyCube()[0],cmds.polyCylinder()[0]])
