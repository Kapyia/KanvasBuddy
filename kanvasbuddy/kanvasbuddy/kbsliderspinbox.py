from PyQt5.QtWidgets import QWidget, QStackedLayout, QProgressBar, QSpinBox
from PyQt5.QtCore import Qt

class KBSliderSpinBox(QWidget):

    def __init__(self, min = 0, max = 100, parent=None):
        super(KBSliderSpinBox, self).__init__(parent)
        self.setMinimumWidth(100)
        self.setFixedHeight(16)
        self.setLayout(QStackedLayout(self))
        self.layout().setStackingMode(QStackedLayout.StackAll)
        self.setCursor(Qt.SplitHCursor)
        self.scaling = 1

        self.progbar = QProgressBar(self)
        self.progbar.setRange(min, max)
        self.progbar.setValue(0)

        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(min, max)
        self.spinbox.setAlignment(Qt.AlignHCenter)
        self.spinbox.setButtonSymbols(self.spinbox.NoButtons)

        self.layout().addWidget(self.spinbox)
        self.layout().addWidget(self.progbar)

        self.spinbox.hide()

        self.spinbox.editingFinished.connect(self.closeSpinBox)
        self.spinbox.lineEdit().returnPressed.connect(self.closeSpinBox)
        self.spinbox.valueChanged.connect(self.updateFormat)
        self.spinbox.valueChanged.connect(self.updateProgBar)

    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            self.setFocus()
            delta = e.pos().x() / self.width()
            self.spinbox.setValue(delta**self.scaling * self.spinbox.maximum())
            self.progbar.setValue(delta * self.progbar.maximum())

    def updateProgBar(self):
        delta = (self.spinbox.value() / self.spinbox.maximum())**(1./self.scaling)
        self.progbar.setValue(delta * self.progbar.maximum())
    
    def mouseMoveEvent(self, e):
        self.mousePressEvent(e)
    
    def mouseDoubleClickEvent(self, e):
        self.openSpinBox()

    def keyPressEvent(self, e):
        if (e.key() == Qt.Key_Return or
            e.key() == Qt.Key_Enter or
            e.key() == Qt.Key_Escape):
            if self.spinbox.isVisible():
                self.closeSpinBox()
        elif e.text().isdecimal():
            if self.spinbox.isHidden():
                self.openSpinBox()
                self.spinbox.lineEdit().keyPressEvent(e)

    def closeSpinBox(self):
        self.spinbox.clearFocus()
        self.spinbox.hide()

    def openSpinBox(self):
        self.spinbox.show()
        self.spinbox.lineEdit().clear()
        self.spinbox.lineEdit().setFocus()
    
    def setRange(self, min, max):
        self.spinbox.setRange(min, max)

    def setScaling(self, s):
        self.scaling = s

    def updateFormat(self):
        self.progbar.setFormat(f"{self.spinbox.prefix()}{self.spinbox.value()}{self.spinbox.suffix()}")
    
    def value(self):
        return self.spinbox.value()
    
    def setValue(self, val):
        self.spinbox.setValue(val)
        self.updateProgBar()

    def setAffixes(self, pre, suf):
        self.spinbox.setPrefix(pre)
        self.spinbox.setSuffix(suf)
        self.updateFormat()

    def connectValueChanged(self, func):
        self.spinbox.valueChanged.connect(func)

    def synchronize(self):
        pass