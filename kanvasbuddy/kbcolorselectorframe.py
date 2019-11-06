# The KanvasBuddy Krita plugin is licensed under CC BY-NC-SA 4.0

# You are free to:
# Share — copy and redistribute the material in any medium or format
# Adapt — remix, transform, and build upon the material

# Under the following terms:
# Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
# NonCommercial — You may not use the material for commercial purposes.
# ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
# No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

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