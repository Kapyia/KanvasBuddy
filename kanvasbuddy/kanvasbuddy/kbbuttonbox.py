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

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QToolButton
from PyQt5.QtGui import QIcon, QPixmap, QImage, QColor
from PyQt5.QtCore import QSize, Qt

class KBButton(QToolButton):

    def __init__(self, size):
        super(KBButton, self).__init__()
        self.setFixedSize(QSize(size, size))
    
    def setIcon(self, icon):
        if isinstance(icon, QIcon):
            super().setIcon(icon)
        elif isinstance(icon, QPixmap):
            super().setIcon(QIcon(icon))
        elif isinstance(icon, QImage):
            super().setIcon(QIcon(QPixmap.fromImage(icon)))
        else:
            raise TypeError(f"Unable to set icon of invalid type {type(icon)}")

    def setColor(self, color):
        if isinstance(color, QColor):
            pxmap = QPixmap(self.iconSize())
            pxmap.fill(color)
            self.setIcon(pxmap)
        else:
            raise TypeError(f"Unable to set color of invalid type {type(color)}")

class KBButtonBox(QWidget):

    def __init__(self, parent, btnSize=32):
        super(KBButtonBox, self).__init__(parent)
        self.setLayout(QHBoxLayout())

        self._buttons = {}
        self.btnSize = btnSize
        
        self.layout().setContentsMargins(0, 0, 0, 0)

    def addButton(self, name):
        self._buttons[name] = KBButton(self.btnSize)
        self._buttons[name].setFocusPolicy(Qt.NoFocus)
        self.layout().addWidget(self._buttons[name])

    def setButtonSize(self, size):
        self.btnSize = size
        for btn in self._buttons:
            btn.setFixedSize(QSize(size, size))

    def button(self, name):
        return self._buttons[name]

