import maya.cmds as cmds

class UI:
    def init(self, winName,height,width):
        self.Window = winName

        if cmds.window(self.Window, exists=True):
            cmds.deleteUI(self.Window, window=True)

        my_win = cmds.window(title=self.Window, widthHeight=(height, width))
        cmds.frameLayout(collapsable=True, label='Generative City')
        cmds.columnLayout(adjustableColumn=True)

        cmds.showWindow(my_win)

    def make_btn(self, argv, **kwargv):
        cmds.button(argv, kwargv)

    def make_f_SliderGrp(self, *argv, kwargv):
        return cmds.floatSliderGrp(f=True, *argv, kwargv)

    def set_f_SliderGrp(self, *argv, kwargv):
        cmds.floatSliderGrp(f=True, e=True, *argv, kwargv)

    def get_f_SliderGrp(self, *argv, kwargv):
        return cmds.floatSliderGrp(q=True, value=True, *argv, kwargv)


        return cmds.intSliderGrp(f=True, *argv, kwargv)

    def set_i_SliderGrp(self, *argv, kwargv):
        cmds.intSliderGrp(f=True, e=True, *argv, kwargv)

    def get_i_SliderGrp(self, *argv, kwargv):
        return cmds.intSliderGrp(q=True, value=True, *argv, kwargv)

    def make_OptMenu(self, menuItems, argv, **kwargv):
        return cmds.optionMenu(argv, kwargv)
        for item in menuItems:
            cmds.menuItem(item)

    def set_OptMenu(self, *argv, kwargv):
        cmds.optionMenu(e=True, *argv, kwargv)

    def get_OptMenu_Item(self, argv):
         return cmds.optionMenu(argv, q=True, v=True)

    def make_Checkbox(self, *argv, kwargv):
        cmds.checkBox(*argv, **kwargv)

    #def set_Checkbox(self, )

    def get_Checkbox(self, argv):
        return cmds.checkBox(argv, q=True, v=True)


    def make_separator(self, ht, st):
        cmds.separator(height = ht, style=st)

#ui = UI('interface',300, 200)
#ui.make_btn(label='buton')