# The KanvasBuddy Krita plugin is licensed under CC BY-NC-SA 4.0

# You are free to:
# Share — copy and redistribute the material in any medium or format
# Adapt — remix, transform, and build upon the material

# Under the following terms:
# Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
# NonCommercial — You may not use the material for commercial purposes.
# ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
# No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

from PyQt5.QtWidgets import QWidget, QSlider, QSpinBox, QGridLayout
from PyQt5.QtCore import Qt

class KBSlider(object):

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

class KBSliderBox(QWidget):

    def __init__(self, parent):
        super(KBSliderBox, self).__init__(parent)
        self.setLayout(QGridLayout())

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setVerticalSpacing(2)
        self.sliders = {}

    def addSlider(self, name, min, max):
        self.sliders[name] = KBSlider(min, max)
        newRow = self.layout().rowCount()
        self.layout().addWidget(self.sliders[name].qslider, newRow, 0)
        self.layout().addWidget(self.sliders[name].qspinbox, newRow, 1)

    def slider(self, name):
        return self.sliders[name]





