
from krita import Krita, PresetChooser

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, Qt

class KBLayerItem(QWidget):

    def __init__(self, node=None):
        super(KBLayerItem, self).__init__()
        self.setLayout(QHBoxLayout(self))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.node = node
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.layout().addWidget(QToolButton())
        self.layout().addWidget(QLabel('Layer Placeholder'))

class KBLayerBox(QScrollArea):

    def __init__(self):
        super(KBLayerBox, self).__init__()
        self.setBackgroundRole(QPalette.Base)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        self.layerList = QWidget(self)
        self.layerList.setLayout(QVBoxLayout())
        self.layerList.layout().setContentsMargins(0, 0, 0, 0)
        self.layerList.layout().setSpacing(0)
        self.layerList.layout().setAlignment(Qt.AlignTop)

        self.setWidget(self.layerList)

    def addLayer(self):
        self.layerList.layout().addWidget(KBLayerItem())

class KBLayerWidget(QWidget):

    def __init__(self, parent):
        super(KBLayerWidget, self).__init__(parent)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        self.layerBox = KBLayerBox()
        self.btn_addLayer = QPushButton('Add')
        self.btn_addLayer.clicked.connect(self.addLayer)

        self.layout().addWidget(self.layerBox)
        self.layout().addWidget(self.btn_addLayer)

    def addLayer(self):
        self.layerBox.addLayer()

    def sizeHint(self):
        return QSize(150, 200)
        


