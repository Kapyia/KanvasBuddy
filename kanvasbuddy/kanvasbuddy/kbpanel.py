from PyQt5.QtWidgets import QWidget, QVBoxLayout

class KBPanel(QWidget):

    def __init__(self, widget):
        super(KBPanel, self).__init__()
        self.wdgt = widget
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.layout().addWidget(self.wdgt)

    def activate(self):
        self.parentWidget().setCurrentWidget(self)

    def widget(self):
        return self.wdgt