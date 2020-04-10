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

from krita import Krita
from .kbsliderspinbox import KBSliderSpinBox

class KBSizeSlider(KBSliderSpinBox):

    def __init__(self, parent=None):
        super(KBSizeSlider, self).__init__(1, 1000, parent)
        self.view = Krita.instance().activeWindow().activeView()
        self.setScaling(3)
        self.setAffixes('Size: ', ' px')
        self.connectValueChanged(self.view.setBrushSize)

    def synchronize(self):
        self.setValue(self.view.brushSize())

        
class KBRotationSlider(KBSliderSpinBox):

    def __init__(self, parent=None):
        super(KBRotationSlider, self).__init__(0, 360, parent)
        self.view = Krita.instance().activeWindow().activeView()
        self.setAffixes('Canvas Rotation: ', '°')
        legacySupportedVersion = 428
        currentVersion = int(Krita.instance().version().replace('.', '')[:3])
        setRotation = None

        if currentVersion > legacySupportedVersion:
            setRotation = lambda: self.view.canvas().setRotation(self.value()) 
        else: 
            # prior to Krita 4.2.9 the API had a bug which made 'setRotation' function as 'rotateCanvas'
            setRotation = lambda: self.view.canvas().setRotation(self.value() - self.view.canvas().rotation())

        self.connectValueChanged(setRotation)

    def synchronize(self):
        self.setValue(self.view.canvas().rotation())


class KBOpacitySlider(KBSliderSpinBox):

    def __init__(self, parent=None):
        super(KBOpacitySlider, self).__init__(parent=parent)
        self.view = Krita.instance().activeWindow().activeView()
        self.setAffixes('Opacity: ', '%')
        self.connectValueChanged(
            lambda: 
                self.view.setPaintingOpacity(self.value()/100)
            )

    def synchronize(self):
        self.setValue(self.view.paintingOpacity()*100)


class KBFlowSlider(KBSliderSpinBox):
    def __init__(self, parent=None):
        super(KBFlowSlider, self).__init__(parent=parent)
        self.view = Krita.instance().activeWindow().activeView()
        self.setAffixes('Flow: ', '%')
        self.connectValueChanged(
            lambda: 
                self.view.setPaintingFlow(self.value()/100)
            )
    
    def synchronize(self):
        self.setValue(self.view.paintingFlow()*100)

