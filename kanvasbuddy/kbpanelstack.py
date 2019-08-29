from krita import Krita, PresetChooser

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, Qt, QEvent

class KBPanel(QWidget):

    def __init__(self, widget=None, main=False):
        super(KBPanel, self).__init__(parent)
        self.setLayout(QVBoxLayout)

        if main: # Valid way of conditionally creating a button?
            self.btnClose = QPushButton(self)
            self.btnClose.setIcon(self.app.action('move_layer_up').icon())
            self.btnClose.setFixedHeight(12)
            self.btnClose.clicked.connect(lambda: self.parentWidget().setCurrentIndex(0))

            self.layout().addWidget(self.btnClose)

    def setWidget(self, w):
        #if self.layout().count() > 1:
        #   remove widget at index 0
        #self.layout().insertWidget(0, w)
        pass

    def setMainPanel(self):
        pass

class KBPanelStack(QStackedWidget):

    def __init__(self, parent=None):
        super(KBPanelStack, self).__init__(parent)
        super().currentChanged.connect(self.currentChanged)
        self.panels = {}
        

    def addPanel(self, name, p):
        self.panels[name] = p

        if not self.count() == 0:
            self.panels[name].setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        
        super().addWidget(self.panels[name])


    def panel(self, name):
        return self.panels[name]


    def currentChanged(self, index):
        for i in range(0, self.count()):
            policy = QSizePolicy.Ignored
            if i == index:
                policy = QSizePolicy.MinimumExpanding
                self.widget(i).setEnabled(True)
            else:
                self.widget(i).setEnabled(False)

            self.widget(i).setSizePolicy(policy, policy)

        self.widget(index).adjustSize()
        self.adjustSize()
        self.parentWidget().adjustSize()
        
    
    def event(self, e):
        ret = super().event(e) # Needs to be called first apparently
        if e.type() == QEvent.WindowDeactivate:
            self.setCurrentIndex(0)
        
        return ret
