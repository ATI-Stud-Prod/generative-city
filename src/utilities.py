import maya.cmds as cmds
import random as random
import math

colorScheme = {
    'custom1': [128,255,0],
    'yellow': [255,255,0],
    'blue': [0,0,255],
    'red': [255, 0, 0],
    'purple': [255,0,255],
    'green': [0, 255, 0]
}

class Shader:
    def __init__(self, node_t):
        self.NodeType=node_t

    def __create_shader(self, naming, node_type):
        node_type = self.NodeType
        mtl = cmds.shadingNode(node_type, name=naming, asShader=True)
        sg = cmds.sets(name="%sSG" % naming, empty=True, renderable=True, noSurfaceShader=True)
        cmds.connectAttr("%s.outColor" % mtl, "%s.surfaceShader" % sg)
        return mtl, sg        

    def set_color(self, key_color, shader_colors):
        meshes = cmds.ls(selection=True, dag=True, type="mesh", noIntermediate=True)
        material, sgrp = self.__create_shader("siege_MTL", self.NodeType)
        cmds.setAttr(material + ".color", shader_colors[key_color][0], shader_colors[key_color][1], shader_colors[key_color][2], type='double3')
        cmds.sets(meshes, forceElement=sgrp)

class Chair:
    # definition d'un pied de la chaise
    # x, y, z, rotateX, rotateY, rotateZ,
    def legs(self, leg_name, ht=4.5):
        cmds.polyCylinder(n='leg%s' % leg_name, sx=20, sy=10, h=ht, r=.15)
        cmds.polyExtrudeFacet( 'leg%s.f[0:19]' % leg_name, kft=True, ltz=.08)
        cmds.polyBevel('leg%s.f[0:19]' % leg_name, offset=0.035)
        cmds.select('leg%s.f[160:179]' % leg_name)
        cmds.scale(0.37,1,1)
        cmds.polyTorus(n = 'knot%s' % leg_name, sr=0.4132, sx=20, sy=20, ch=1)
        cmds.scale(0.162, 0.162, 0.162, 'knot%s' % leg_name)
        cmds.rotate(0,0,90,'knot%s' % leg_name)
        cmds.move(0, 2.138, 0,'knot%s' % leg_name)
        cmds.polyUnite('knot%s' % leg_name, 'leg%s' % leg_name, n='n_leg%s' % leg_name)
        # self.set_leg_pos(x, y, z, rotateX, rotateY, rotateZ)

    # positionement d'un pied
    def set_leg_pos(self, x, y, z, rotateX, rotateY, rotateZ):
        # connaitre la position d'un vertex
        #posV = cmds.xform("pSphere1.vtx[100]",q=True,t=True)
        cmds.move(x, y, z)
        cmds.rotate(rotateX, rotateY, rotateZ)

    # definition du siege de la chaise
    def seat(self, sname, height=40, width=15, depth=40):
        cmds.polySphere(n = 'sphere%s' % sname, sx=40, sy=15, r=1)
        cmds.scale(1.451, 0.214, 1.451, 'sphere%s' % sname)
        cmds.polyTorus(n = 'circlemetal%s' % sname, sr=0.032, sx=30, sy=20, r=0.45, ch=1)
        cmds.scale(3.221, 3.221, 3.221, 'circlemetal%s' % sname)
        cmds.polyUnite('sphere%s' % sname, 'circlemetal%s' % sname, n='full%s' % sname)

    # definition de la position du siege
    def set_seat_pos(self, x, y, z, rotation):
        cmds.move(x, y, z)
        cmds.rotate(rotation, 0, 0)

    # definition d'un barreau
    def barreau(self, x, y, z, scaleY, name, rotateX = 0, rotateY = 0, rotateZ = 90):
        cmds.polyCylinder(n= name)
        cmds.move(x,y,z)
        cmds.scale(0.142, scaleY, 0.142)
        cmds.rotate(rotateX, rotateY, rotateZ)

    def get_height(self, longueur_pied, angle_prime): # longueur_pieds equivalent a l'hypotenuse
        return longueur_pied * math.cos(math.radians(angle_prime))

    def rotate_leg(self, objname, val):
        cmds.setAttr(objname+'.rotateX',val)

    def move_leg(self, objname, axis, val):
        cmds.setAttr(objname+'.translate'+axis.upper(), val)

    def set_chair_to_o():
        cmds.xform()


    def grp_all(self):
        cmds.group(w=True)

    # def pos_legs_vert():
    #     if make_check_box():
    #         return [-1.295, 0.54]
    #     else:
    #         return [-0.43, 0]

    # supprimer l'historique
    def supprimer_histo(self):
        cmds.select(all = True)
        cmds.delete(constructionHistory = True)

class UI:
    def __init__(self, name):
        self.Window = name

        if cmds.window(self.Window, exists=True):
            cmds.deleteUI(self.Window, window=True)

        my_win = cmds.window(title=self.Window, widthHeight=(300, 200))

        cmds.columnLayout(adjustableColumn=True)

        cmds.showWindow(my_win)

    def make_btn(self, btn_name, btn_lbl, btnCmd):
        cmds.button(btn_name,label=btn_lbl, command=btnCmd)

    def make_slider(self, sld_name, lbl_name):
        return cmds.floatSliderGrp(sld_name, label=lbl_name, field=True, minValue =4.5, maxValue =10.0, value = 4.5)

    def get_slider(self, sld_name):
        return cmds.floatSliderGrp(sld_name, query=True, value=True)

    def make_optmenu(self, optMenName, optMenLbl, menuItems):
        cmds.optionMenu(optMenName, label=optMenLbl)
        for item in menuItems:
            cmds.menuItem(item)

    def set_optmenu(self, optname, createColor):
        cmds.optionMenu(optname, e=True, changeCommand=createColor)

    def get_optmenu_item(self, optname):
         return cmds.optionMenu(optname, q=True, v=True)

    def make_checkbox(self, chk_name, chk_lbl):
        cmds.checkBox(chk_name, label=chk_lbl, onCommand=self.__lock_haut_pied)

    def get_checkbox(self, chk_name):
        return cmds.checkBox(chk_name, q=True, v=True)


    def make_separator(self, ht):
        cmds.separator(height = ht, style='out')

    def __lock_haut_pied(self, value):
        cmds.floatSliderGrp('sliderHautChaise', e=True, enable=value)

class Shader:
    def __init__(self, node_t):
        self.NodeType=node_t

    def __create_shader(self, naming, node_type):
        node_type = self.NodeType
        mtl = cmds.shadingNode(node_type, name=naming, asShader=True)
        sg = cmds.sets(name="%sSG" % naming, empty=True, renderable=True, noSurfaceShader=True)
        cmds.connectAttr("%s.outColor" % mtl, "%s.surfaceShader" % sg)
        return mtl, sg

    def set_color(self, key_color, shader_colors):
        meshes = cmds.ls(selection=True, dag=True, type="mesh", noIntermediate=True)
        material, sgrp = self.__create_shader("siege_MTL", self.NodeType)
        cmds.setAttr(material + ".color", shader_colors[key_color][0], shader_colors[key_color][1], shader_colors[key_color][2], type='double3')
        cmds.sets(meshes, forceElement=sgrp)

colorScheme = {
    'yellow': [255,255,0],
    'blue': [0,0,255],
    'red': [255, 0, 0],
    'purple': [255,0,255],
    'green': [0, 255, 0]
}

user = UI('Chaise')
user.make_btn('btn_chaise', 'Creer Chaise', 'chaise()')
user.make_slider('sliderHautChaise','hauteur pied')
user.make_slider('sliderLargeSiege','largeur siege')
user.make_slider('sliderProfondSiege', 'profondeur siege')
user.make_slider('sliderHautDoss', 'Hauteur dossier')
user.make_slider('sliderLargeDoss', 'largeur dossier')
user.make_separator(5)
user.make_checkbox('verti_check','Pied Vertical')

shade = Shader('blinn')
user.make_optmenu('optSetColor', 'Colors', colorScheme.keys())
colorFunc = lambda x: shade.set_color(user.get_optmenu_item('optSetColor'), colorScheme)
user.set_optmenu('optSetColor', colorFunc)
user.make_btn('btn_suppr', 'Supprimer Chaise', 'cmds.delete()')

# cmds.move(0, chair.Height + hAssise/2, 0,)
def chaise():
    chair = Chair()

    hLegs = user.get_slider('sliderHautChaise')

    chair.legs('arriere_droit', hLegs)#neg
    chair.set_leg_pos(-1.039, 0, 0, -30, 0, 0)

    chair.legs('arriere_gauche',hLegs)
    chair.set_leg_pos(1.039, 0, 0, -30, 0, 0)

    chair.legs('devant_droit', hLegs)#pos
    chair.set_leg_pos(0.75, 0, -0.43, 30, 0, 0)

    chair.legs('devant_gauche', hLegs)
    chair.set_leg_pos(-0.75, 0, -0.43, 30, 0, 0)

    wSeat = user.get_slider('sliderLargeSiege')

    chair.seat('siege',wSeat, dSeat) # siege de la chaise
    chair.set_seat_pos(0, 2.075, -0.38, 0)

    hBack = user.get_slider('sliderHautDoss')
    wBack = user.get_slider('sliderLargeDoss')

    chair.seat('dossier',wBack, hBack) # dossier de la chaise
    chair.set_seat_pos(0, 4.15, 1, -84.776)

    chair.barreau(0, -0.92,  0.536, 1.05,'b_arriere') # barreau arriere 0.536
    chair.barreau(0, -0.92, -0.967, 0.76, 'b_devant') # barreau de devant -0.967
    chair.barreau(0, 1.851, 0.631, 0.7, 'sous_siege') # barreau sous le siege
    chair.barreau(-0.6, 2.5, 1, 0.81, 'b_droit', 5, 0, 4) # barreau droit du dossier
    chair.barreau(0.6, 2.5, 1, 0.81, 'b_gauche', 5, 0, -4)  # barreau gauche du dossier
    chair.supprimer_histo()
    chair.grp_all()

