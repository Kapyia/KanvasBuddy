# This file is part of KanvasBuddy.

# KanvasBuddy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# KanvasBuddy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with KanvasBuddy. If not, see <https://www.gnu.org/licenses/>.

# CONTRIBUTORS:
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
            importlib.reload(uikanvasbuddy) # FOR TESTING ONLY
            self.isActive = True
            ui = uikanvasbuddy.UIKanvasBuddy(self)
            ui.launch()


    def setIsActive(self, b):
        if isinstance(b, bool):
            self.isActive = b
        else:
            raise TypeError("invalid argument; active state must be a boolean")

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(KanvasBuddy(Krita.instance()))