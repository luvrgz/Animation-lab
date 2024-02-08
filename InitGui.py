import FreeCADGui as Gui


class AnimationLab(Workbench):
    MenuText = "AnimationLab"
    ToolTip = "A description of my workbench"
    Icon = "icons\\recompute.xpm"

    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        import animations.animation
        list_commands = ["AddTrajectory"]
        self.appendToolbar("My Commands", list_commands)  # creates a new toolbar with your commands
        self.appendMenu("My New Menu", list_commands)  # creates a new menu
        self.appendMenu(["An existing Menu", "My submenu"], list_commands)  # appends a submenu to an existing menu

    def Activated(self):
        """This function is executed when the workbench is activated"""
        print("MY WORKBENCH IS ACTIVATED")
        from PySide import QtCore, QtGui

        class DocumentFilter(QtCore.QObject):
            def eventFilter(self, obj, ev):
                print("Event:", ev.type())
                return False

        print("Event filter...", end="")
        mw = Gui.getMainWindow()
        views = mw.findChildren(QtGui.QMainWindow)
        print(views)
        print(views[0].metaObject().className())
        view = views[0]
        f = DocumentFilter()
        print(dir(f))
        view.installEventFilter(f)
        print(dir(view))
        print("...Finished")
        return

    def Deactivated(self):
        """This function is executed when the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands", self.list)  # add commands to the context menu

    def GetClassName(self):
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"


Gui.addWorkbench(AnimationLab())