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

from .kbsliderspinbox import KBSliderSpinBox
from .kbsliderpresets import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout

class KBSliderBar(QWidget):

    def __init__(self, parent):
        super(KBSliderBar, self).__init__(parent)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(2, 0, 2, 0)
        self.layout().setSpacing(4)

        self._sliders = {}
        self._presets = {
            'canvasRotation': KBRotationSlider,
            'brushOpacity': KBOpacitySlider,
            'brushFlow': KBFlowSlider,
            'brushSize': KBSizeSlider
        }

    def createSlider(self, ID, min, max): # Redundant?
        self._sliders[ID] = KBSliderSpinBox(min, max)
        self.layout().addWidget(self._sliders[ID])

    def addSlider(self, ID):
        self._sliders[ID] = self._presets[ID]()
        self.layout().addWidget(self._sliders[ID])

    def slider(self, ID):
        return self._sliders[ID]

    def synchronizeSliders(self):
        for slider in self._sliders:
            self._sliders[slider].synchronize()