# This file is part of KanvasBuddy.

# KanvasBuddy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

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
        self.qspinbox.valueChanged.connect(func)

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





