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
from PyQt5.QtCore import QSize, Qt, QEvent

class KBPanel(QWidget):

    def __init__(self, index, widget=None):
        super(KBPanel, self).__init__()
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        
        if widget:
            self.layout().addWidget(widget)

        if index > 0: # Valid way of conditionally creating a button?
            self.btnClose = QPushButton(self)
            self.btnClose.setIcon(Krita.instance().action('move_layer_up').icon())
            self.btnClose.setIconSize(QSize(10, 10))
            self.btnClose.setFixedHeight(12)
            self.btnClose.clicked.connect(lambda: self.parentWidget().setCurrentIndex(0))

            self.layout().addWidget(self.btnClose)


    def setWidget(self, w):
        if self.layout().count() > 1:
            self.layout().removeItem(self.layout().itemAt(0))
        self.layout().insertWidget(0, w)


class KBPanelStack(QStackedWidget):

    def __init__(self, parent=None):
        super(KBPanelStack, self).__init__(parent)
        super().currentChanged.connect(self.currentChanged)
        self.panels = {}
        

    def addPanel(self, name, widget):
        self.panels[name] = KBPanel(self.count(), widget)

        if not self.count() == 0:
            self.panels[name].setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        
        super().addWidget(self.panels[name])


    def panel(self, name):
        return self.panels[name]


    def currentChanged(self, index):
        for i in range(0, self.count()):
            policy = QSizePolicy.Ignored
            if i == index:
                policy = QSizePolicy.MinimumExpanding
                self.widget(i).setEnabled(True)
            else:
                self.widget(i).setEnabled(False)

            self.widget(i).setSizePolicy(policy, policy)

        self.widget(index).adjustSize()
        self.adjustSize()
        self.parentWidget().adjustSize()
        
    
    def event(self, e):
        ret = super().event(e) # Needs to be called first, apparently
        if e.type() == QEvent.WindowDeactivate:
            self.setCurrentIndex(0)
        
        return ret
