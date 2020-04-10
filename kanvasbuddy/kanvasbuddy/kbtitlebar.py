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

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QToolButton, QStyle
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, Qt

from krita import Krita

class KBTitleBar(QWidget):

    def __init__(self, parent):
        super(KBTitleBar, self).__init__(parent)
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(2, 1, 2, 1)
        self.pressing = False

        self.title = QLabel("KanvasBuddy")
        font = self.font()
        font.setPixelSize(9)
        self.title.setFont(font)
        self.title.setStyleSheet("""
            color: grey;
        """)

        self.btn_close = QToolButton()
        self.btn_close.setFixedSize(10, 10)
        self.btn_close.setIconSize(QSize(7,7))
        self.btn_close.clicked.connect(self.parent.close)
        self.btn_close.setIcon(parent.style().standardIcon(QStyle.SP_DockWidgetCloseButton))
        self.btn_close.setFocusPolicy(Qt.NoFocus)

        self.btn_pinned_mode = QToolButton()
        self.btn_pinned_mode.setCheckable(True)
        self.btn_pinned_mode.setToolTip("Toggle pinned panel mode")
        self.btn_pinned_mode.setFixedSize(10, 10)
        self.btn_pinned_mode.setIconSize(QSize(7,7))
        self.btn_pinned_mode.clicked.connect(self.parent.togglePinnedMode)
        self.btn_pinned_mode.setIcon(Krita.instance().icon('light_krita_tool_reference_images.svg'))
        self.btn_pinned_mode.setFocusPolicy(Qt.NoFocus)

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_pinned_mode)
        self.layout.addWidget(self.btn_close)
        self.setLayout(self.layout)


    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True


    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end


    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False