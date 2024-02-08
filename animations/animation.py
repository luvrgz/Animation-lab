import FreeCAD
import FreeCADGui

class AddTrajectory:
    """My new command"""

    def GetResources(self):
        return {"Pixmap": "icons\\recompute.xpm",
                "MenuText": "Update",
                "ToolTip": "Update the current document"}

    def Activated(self):
        """Do something here"""
        import animation_object as ao
        anim_obj = ao.AnimationObject()


    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

FreeCADGui.addCommand("Add trajectory", AddTrajectory())