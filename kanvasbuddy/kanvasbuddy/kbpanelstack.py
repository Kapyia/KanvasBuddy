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

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QStackedWidget, QSizePolicy
from PyQt5.QtCore import QSize, QEvent, pyqtSignal

from .kbbuttonbar import KBButtonBar
from .kbpanel import KBPanel
from .kbpresetchooser import KBPresetChooser

class KBPanelStack(QStackedWidget):
    presetChanged = pyqtSignal()

    def __init__(self, parent=None):
        super(KBPanelStack, self).__init__(parent)
        super().currentChanged.connect(self.currentChanged)
        self._panels = {}
        self._widgetParents = {}
        self._pinned_mode = False
        
        self.mainPanel = QWidget()
        self.mainPanel.setLayout(QVBoxLayout())
        self.mainPanel.layout().setContentsMargins(4, 4, 4, 4)

        self.navBtns = KBButtonBar(32)

        self.mainPanel.layout().addWidget(self.navBtns)
        self.addPanel('main', self.mainPanel)


    def addPanel(self, ID, widget):
        panel = KBPanel(widget)

        if self.count() > 0:
            panel.layout().addWidget(KBPanelCloseButton())

        self._panels[ID] = panel
        super().addWidget(panel)


    def loadPanel(self, data):
        ID = data['id']
        if ID == 'PresetDocker': # This is ugly, but necessary until the Krita API opens a proper 'presetChanged' signal
            pc = KBPresetChooser()
            pc.presetSelected.connect(self.brushPresetChanged)
            pc.presetClicked.connect(self.brushPresetChanged)
            self.addPanel(ID, pc)
        else:
            qwindow = Krita.instance().activeWindow().qwindow()
            parent = qwindow.findChild(QWidget, ID)

            self._widgetParents[ID] = parent
            self.addPanel(ID, parent.widget())

            if data['size']:
                self.panel(ID).setSizeHint(data['size'])

        self.navBtns.loadButton(data, self.panel(ID).activate)
        

    def dismantle(self):
        for parent in self._widgetParents:
            self._widgetParents[parent].setWidget(self.panel(parent).widget())
            self._widgetParents[parent].widget().setEnabled(True)


    def panel(self, name):
        return self._panels[name]


    def main(self):
        return self.mainPanel


    def togglePinnedMode(self):
        self._pinned_mode = not self._pinned_mode


    def currentChanged(self, index):
        for i in range(0, self.count()):
            policy = QSizePolicy.Ignored
            if i == index:
                policy = QSizePolicy.Expanding
                self.widget(i).setEnabled(True)
            else:
                self.widget(i).setDisabled(False)

            self.widget(i).setSizePolicy(policy, policy)
            self.widget(i).updateGeometry()

        self.adjustSize()
        self.parentWidget().adjustSize()
        
    
    def event(self, e):
        r = super().event(e) # Get the return value of the parent class' event method first
        if (e.type() == QEvent.WindowDeactivate and
            not self._pinned_mode):
            self.setCurrentIndex(0)
        
        return r


    def brushPresetChanged(self, preset):
        Krita.instance().activeWindow().activeView().activateResource(
            self.panel('PresetDocker').widget().currentPreset()
            )
        self.presetChanged.emit()


class KBPanelCloseButton(QPushButton):

    def __init__(self, parent=None):
        super(KBPanelCloseButton, self).__init__(parent)
        self.setIcon(Krita.instance().action('move_layer_up').icon())
        self.setIconSize(QSize(10, 10))
        self.setFixedHeight(12)
        self.clicked.connect(lambda: self.parentWidget().parentWidget().setCurrentIndex(0))