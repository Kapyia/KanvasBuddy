# The KanvasBuddy Krita plugin is licensed under CC BY-NC-SA 4.0

# You are free to:
# Share — copy and redistribute the material in any medium or format
# Adapt — remix, transform, and build upon the material

# Under the following terms:
# Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
# NonCommercial — You may not use the material for commercial purposes.
# ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
# No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

# CONTRIBUTORS
# Kapyia @ https://krita-artists.org/ 

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QToolButton
from PyQt5.QtGui import QIcon, QPixmap, QImage, QColor
from PyQt5.QtCore import QSize

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
        self.layout().addWidget(self._buttons[name])

    def setButtonSize(self, size):
        self.btnSize = size
        for btn in self._buttons:
            btn.setFixedSize(QSize(size, size))

    def button(self, name):
        return self._buttons[name]

