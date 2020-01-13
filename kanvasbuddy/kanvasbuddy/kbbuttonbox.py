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

from krita import *
from .kbbutton import KBButton

from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtCore import QSize, Qt

class KBButtonBar(QWidget):

    def __init__(self, btnSize, parent=None):
        super(KBButtonBar, self).__init__(parent)
        self.setLayout(QHBoxLayout())

        self._buttons = {}
        self.btnSize = btnSize
        
        self.layout().setContentsMargins(0, 0, 0, 0)


    def addButton(self, ID):
        self._buttons[ID] = KBButton(self.btnSize)
        self._buttons[ID].setFocusPolicy(Qt.NoFocus)
        self.layout().addWidget(self._buttons[ID])
    

    def loadButton(self, data, onClick):
        btn = KBButton(self.btnSize)
        btn.setFocusPolicy(Qt.NoFocus)
        btn.setIcon(Application.icon(data['icon']))
        btn.clicked.connect(onClick)

        self._buttons[data['id']] = btn
        self.layout().addWidget(btn)

    def setButtonSize(self, size):
        self.btnSize = size
        for btn in self._buttons:
            btn.setFixedSize(QSize(size, size))

    def button(self, ID):
        return self._buttons[ID]