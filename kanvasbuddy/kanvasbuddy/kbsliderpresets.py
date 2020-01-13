from krita import Krita
from .kbsliderspinbox import KBSliderSpinBox

class KBSizeSlider(KBSliderSpinBox):

    def __init__(self, parent=None):
        super(KBSizeSlider, self).__init__(1, 1000, parent)
        self.view = Krita.instance().activeWindow().activeView()
        self.setScaling(3)
        self.setAffixes('Size: ', 'px')
        self.connectValueChanged(self.view.setBrushSize)

    def synchronize(self):
        self.setValue(self.view.brushSize())

        
class KBRotationSlider(KBSliderSpinBox):

    def __init__(self, parent=None):
        super(KBRotationSlider, self).__init__(0, 360, parent)
        self.view = Krita.instance().activeWindow().activeView()
        self.setAffixes('Canvas Rotation: ', '°')
        self.connectValueChanged(
            lambda:
                # 'setRotation' is actually 'rotateCanvas'
                self.view.canvas().setRotation(self.value() - self.view.canvas().rotation()) 
            )

    def synchronize(self):
        self.setValue(self.view.canvas().rotation())


class KBOpacitySlider(KBSliderSpinBox):

    def __init__(self, parent=None):
        super(KBOpacitySlider, self).__init__(parent=parent)
        self.view = Krita.instance().activeWindow().activeView()
        self.setAffixes('Opacity: ', '%')
        self.connectValueChanged(
            lambda: 
                self.view.setPaintingOpacity(self.value()/100)
            )

    def synchronize(self):
        self.setValue(self.view.paintingOpacity()*100)


class KBFlowSlider(KBSliderSpinBox):
    def __init__(self, parent=None):
        super(KBFlowSlider, self).__init__(parent=parent)
        self.view = Krita.instance().activeWindow().activeView()
        self.setAffixes('Flow: ', '%')
        self.connectValueChanged(
            lambda: 
                self.view.setPaintingFlow(self.value()/100)
            )
    
    def synchronize(self):
        self.setValue(self.view.paintingFlow()*100)

