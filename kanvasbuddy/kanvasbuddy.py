# This script is licensed CC 0 1.0, so that you can learn from it.

# ------ CC 0 1.0 ---------------

# The person who associated a work with this deed has dedicated the
# work to the public domain by waiving all of his or her rights to the
# work worldwide under copyright law, including all related and
# neighboring rights, to the extent allowed by law.

# You can copy, modify, distribute and perform the work, even for
# commercial purposes, all without asking permission.

# https://creativecommons.org/publicdomain/zero/1.0/legalcode

import importlib

from krita import Krita, Extension
from PyQt5.QtWidgets import QMessageBox
from . import uikanvasbuddy

class KanvasBuddy(Extension):

    def __init__(self, parent):
        super(KanvasBuddy, self).__init__(parent)

    def setup(self):
        pass

    def createActions(self, window): # Called by Krita on startup      
        action = window.createAction("kanvasbuddy", "KanvasBuddy")
        action.setToolTip("Minimal toolbox for speed painting")
        action.triggered.connect(self.launchInterface)

    def launchInterface(self):
        if Krita.instance().activeDocument():
            importlib.reload(uikanvasbuddy) # Remove for release
            ui = uikanvasbuddy.UIKanvasBuddy(self)
            ui.launch()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setWindowTitle('KanvasBuddy')
            msg.setText("No active documents found. \n\n" +  
                        "KanvasBuddy requires at least one active document to launch.")
            # msg.setInformativeText("KanvasBuddy requires at least one active document to launch.")

            msg.exec_()
        
# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(KanvasBuddy(Krita.instance()))