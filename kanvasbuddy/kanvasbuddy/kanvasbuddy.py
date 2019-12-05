# The KanvasBuddy Krita plugin is licensed under CC BY-NC-SA 4.0

# You are free to:
# Share — copy and redistribute the material in any medium or format
# Adapt — remix, transform, and build upon the material

# Under the following terms:
# Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
# NonCommercial — You may not use the material for commercial purposes.
# ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
# No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

# CONTRIBUTORS
# Kapyia @ https://krita-artists.org/ 

import importlib

from krita import Krita, Extension
from PyQt5.QtWidgets import QMessageBox
from . import uikanvasbuddy

class KanvasBuddy(Extension):

    def __init__(self, parent):
        super(KanvasBuddy, self).__init__(parent)
        self.isActive = False


    def setup(self):
        pass


    def createActions(self, window): # Called by Krita on startup
        action = window.createAction("kanvasbuddy", "KanvasBuddy")
        action.setToolTip("Minimal toolbox for speed painting")
        action.triggered.connect(self.launchInterface)


    def launchInterface(self):
        if not Krita.instance().activeDocument():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowTitle('KanvasBuddy')
            msg.setText("No active documents found. \n\n" +  
                        "KanvasBuddy requires at least one active document to launch.")
            msg.exec_()
        elif self.isActive:
            pass
        else:
            # importlib.reload(uikanvasbuddy) # FOR TESTING ONLY
            self.isActive = True
            ui = uikanvasbuddy.UIKanvasBuddy(self)
            ui.launch()


    def setIsActive(self, b):
        if isinstance(b, bool):
            self.isActive = b
        else:
            raise TypeError("invalid argument; must be a boolean")

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(KanvasBuddy(Krita.instance()))