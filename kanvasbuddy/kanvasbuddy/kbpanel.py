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

from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import QSize

class KBPanel(QWidget):

    def __init__(self, widget):
        super(KBPanel, self).__init__()
        self.wdgt = widget
        self.size = None
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.layout().addWidget(self.wdgt)


    def activate(self):
        self.parentWidget().setCurrentWidget(self)


    def widget(self):
        return self.wdgt


    def setSizeHint(self, size):
        self.size = QSize(size[0], size[1]+12)


    def sizeHint(self):
        if self.size:
            return self.size
        else:
            return self.wdgt.sizeHint()
    

    