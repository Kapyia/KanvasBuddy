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

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QStackedWidget, QSizePolicy, QMessageBox
from PyQt5.QtCore import QSize, Qt, QEvent


def boop(text): # Print a message to a dialog box
    msg = QMessageBox()
    msg.setText(str(text))
    msg.exec_()


class KBPanelCloseButton(QPushButton):

    def __init__(self, parent=None):
        super(KBPanelCloseButton, self).__init__(parent)
        self.setIcon(Krita.instance().action('move_layer_up').icon())
        self.setIconSize(QSize(10, 10))
        self.setFixedHeight(12)


class KBPanel(QWidget):

    def __init__(self, widget):
        super(KBPanel, self).__init__()
        self.w = widget
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.layout().addWidget(widget)

    def activate(self):
        self.parentWidget().setCurrentWidget(self)

    def widget(self):
        return self.w


class KBPanelStack(QStackedWidget):

    def __init__(self, parent=None):
        super(KBPanelStack, self).__init__(parent)
        super().currentChanged.connect(self.currentChanged)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.panels = {}


    def addPanel(self, name, widget):
        panel = KBPanel(widget)

        if self.count() > 0:
            btnClose = KBPanelCloseButton()
            btnClose.clicked.connect(lambda: self.setCurrentIndex(0))

            panel.layout().addWidget(btnClose)

        self.panels[name] = panel
        super().addWidget(panel)

    
    def panel(self, name):
        return self.panels[name]

    def currentChanged(self, index):
        for i in range(0, self.count()):
            if i == index:
                self.widget(i).show()
                self.widget(i).setEnabled(True)
            else:
                self.widget(i).hide()
                self.widget(i).setEnabled(False)

            # self.widget(i).setSizePolicy(policy, policy)
            self.adjustSize()
            self.parentWidget().adjustSize()

        
        
    
    def event(self, e):
        ret = super().event(e) # Needs to be called first apparntly
        if e.type() == QEvent.WindowDeactivate:
            self.setCurrentIndex(0)
        
        return ret