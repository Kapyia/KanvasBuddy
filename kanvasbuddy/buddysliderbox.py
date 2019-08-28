from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class BuddySlider(object):

    def __init__(self, min, max):
        self.qslider = QSlider(Qt.Horizontal)
        self.qslider.setMinimumWidth(100)

        self.qspinbox = QSpinBox()
        self.qspinbox.setAlignment(Qt.AlignHCenter)
        self.qspinbox.setButtonSymbols(2)
        font = self.qspinbox.font()
        font.setPixelSize(9)
        self.qspinbox.setFont(font)
        self.qspinbox.setFixedHeight(20)

        self.setRange(min, max)

        self.qslider.valueChanged.connect(self.qspinbox.setValue)
        self.qspinbox.valueChanged.connect(self.qslider.setValue)

    def setPrefix(self, prefix):
        self.qspinbox.setPrefix(prefix)

    def setSuffix(self, suffix):
        self.qspinbox.setSuffix(suffix)
    
    def setAffixes(self, prefix, suffix):
        self.qspinbox.setPrefix(prefix)
        self.qspinbox.setSuffix(suffix)

    def setRange(self, min, max):
        self.qslider.setRange(min, max)
        self.qspinbox.setRange(min, max)
    
    def setValue(self, value):
        self.qslider.setValue(value)
    
    def value(self):
        return self.qslider.value()

    def connectValueChanged(self, func):
        self.qslider.valueChanged.connect(func)

class BuddySliderBox(QWidget):

    def __init__(self, parent):
        super(BuddySliderBox, self).__init__(parent)
        self.setLayout(QGridLayout())

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setVerticalSpacing(2)
        self.sliders = {}

    def addSlider(self, name, min, max):
        self.sliders[name] = BuddySlider(min, max)
        newRow = self.layout().rowCount()
        self.layout().addWidget(self.sliders[name].qslider, newRow, 0)
        self.layout().addWidget(self.sliders[name].qspinbox, newRow, 1)
    def slider(self, name):
        return self.sliders[name]





