import FreeCAD


class AnimationObject:
    def __init__(self):
        self.trajectory = None

        ob = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "trajectory")
        self.name = ob.Name
        ob.addProperty("App::PropertyString", "Type", "ConstraintInfo").Type = "oui"