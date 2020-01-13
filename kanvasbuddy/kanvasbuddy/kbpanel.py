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
    

    