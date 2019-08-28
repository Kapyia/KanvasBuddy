from krita import Krita, PresetChooser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, Qt

class KBPresetChooser(PresetChooser):

    def __init__(self, parent=None):
        super(KBPresetChooser, self).__init__(parent)
        self.layout().itemAt(0).widget().layout().itemAt(4).removeItem(self.layout().itemAt(0).widget().layout().itemAt(4).itemAtPosition(0,0))
        self.layout().itemAt(0).widget().layout().itemAt(4).removeItem(self.layout().itemAt(0).widget().layout().itemAt(4).itemAtPosition(0,1))
        self.layout().itemAt(0).widget().layout().removeItem(self.layout().itemAt(0).widget().layout().itemAt(4))


