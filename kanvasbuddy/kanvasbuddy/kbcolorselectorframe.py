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

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QSize

class KBColorSelectorFrame(QWidget):
    def __init__(self, w=None):
        super(KBColorSelectorFrame, self).__init__()
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        if w:
            self.layout().addWidget(w)

    def sizeHint(self):
        return QSize(290, 290)

    def setWidget(self, w):
        self.layout().addWidget(w)

    def widget(self):
        return self.layout().itemAt(0).widget()