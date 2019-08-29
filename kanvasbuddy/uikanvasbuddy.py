# WISHLIST:
#   Wrapper for KisColorSelector 
#   Access to "Zoom to Page" or the canvas view size

# TODO:
#   Better icon for color picker
#   Resize Up Arrow Icon for the button that closes larger widgets
#   Make a "large widget" widget that has the close button built in
#   Layer box
#

from krita import Krita, PresetChooser

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, Qt
from . import (
    kbsliderbox as sldbox, 
    kbbuttonbox as btnbox, 
    kbtitlebar as title,
    kblayerbox as lyrbox,
    presetchooser as prechooser,
    kbpanelstack as pnlstk
)
import importlib

class colorSelectorHolder(QWidget):

    def __init__(self, w=None):
        super(colorSelectorHolder, self).__init__()
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        if w:
            self.setWidget(w)

    def sizeHint(self):
        return QSize(250, 250)

    def setWidget(self, w):
        self.layout().addWidget(w)

    def widget(self):
        return self.layout().itemAt(0).widget()

class UIKanvasBuddy(QDialog):

    def __init__(self, kbuddy):
        super(UIKanvasBuddy, self).__init__(Krita.instance().activeWindow().qwindow())
        importlib.reload(sldbox)
        importlib.reload(btnbox)
        importlib.reload(title)
        importlib.reload(lyrbox)
        importlib.reload(prechooser)
        importlib.reload(pnlstk)

        self.app = Krita.instance()
        self.view = self.app.activeWindow().activeView()
        self.kbuddy = kbuddy
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)
        
        self.mainWidget = pnlstk.KBPanelStack(self)
        
        self.layout().addWidget(title.KBTitleBar(self))
        self.layout().addWidget(self.mainWidget)
        
        self.mainPanel = QWidget(self)
        self.mainPanel.setLayout(QVBoxLayout())
        self.mainPanel.layout().setContentsMargins(4, 4, 4, 4)

        
        # PANEL BUTTONS
        self.panelButtons = btnbox.KBButtonBox(self)

        self.panelButtons.addButton('presets')
        self.panelButtons.button('presets').setIcon(self.app.icon('light_paintop_settings_01'))
        self.panelButtons.button('presets').clicked.connect(lambda: self.mainWidget.setCurrentIndex(1))

        self.panelButtons.addButton('color')
        self.panelButtons.button('color').setIcon(self.app.icon('light_krita_tool_color_picker'))
        # self.panelButtons.button('color').clicked.connect(self.app.action('show_color_selector').trigger)
        self.panelButtons.button('color').clicked.connect(lambda: self.mainWidget.setCurrentIndex(2))

        self.panelButtons.addButton('layers')     
        self.panelButtons.button('layers').setIcon(self.app.icon('duplicatelayer'))
        self.panelButtons.button('layers').clicked.connect(lambda: self.mainWidget.setCurrentIndex(3))


        # WIDGET: PRESET CHOOSER        
        self.presetChooser = PresetChooser()
        self.presetChooser.presetSelected.connect(self.setPreset)
        self.presetChooser.presetClicked.connect(self.setPreset)

        self.btn_back = QPushButton(self)
        self.btn_back.setIcon(self.app.action('move_layer_up').icon())
        self.btn_back.setFixedHeight(12)
        self.btn_back.clicked.connect(lambda: self.mainWidget.setCurrentIndex(0))

        self.presetChooser.layout().itemAt(0).widget().layout().removeItem(self.presetChooser.layout().itemAt(0).widget().layout().itemAt(4))
        self.presetChooser.layout().itemAt(0).widget().layout().addWidget(self.btn_back)


        # WIDGET: LAYER BOX
        self.btn_exit = QPushButton(self)
        self.btn_exit.setIcon(self.app.action('move_layer_up').icon())
        self.btn_exit.setFixedHeight(12)
        self.btn_exit.clicked.connect(lambda: self.mainWidget.setCurrentIndex(0))

        self.layerList = lyrbox.KBLayerWidget(self)
        self.layerList.layout().addWidget(self.btn_exit)


        # PRESET PROPERTIES
        self.brushProperties = sldbox.KBSliderBox(self)

        self.brushProperties.addSlider('opacity', 0, 100)
        self.brushProperties.slider('opacity').setAffixes('Op: ', '%')
        self.brushProperties.slider('opacity').connectValueChanged(
            lambda: 
                self.view.setPaintingOpacity(self.brushProperties.slider('opacity').value()/100)
            )

        self.brushProperties.addSlider('size', 0, 1000)
        self.brushProperties.slider('size').setAffixes('Sz: ', ' px')
        self.brushProperties.slider('size').connectValueChanged(self.view.setBrushSize)


        # CANVAS OPTIONS
        self.canvasOptions = btnbox.KBButtonBox(self, 16)

        self.canvasOptions.addButton('presets')
        self.canvasOptions.button('presets').clicked.connect(self.app.action('view_show_canvas_only').trigger)
        self.canvasOptions.button('presets').setIcon(self.app.action('view_show_canvas_only').icon())

        self.canvasOptions.addButton('mirror')
        self.canvasOptions.button('mirror').clicked.connect(self.app.action('mirror_canvas').trigger)
        self.canvasOptions.button('mirror').setIcon(self.app.action('mirror_canvas').icon())

        self.canvasOptions.addButton('reset_view')
        self.canvasOptions.button('reset_view').clicked.connect(self.app.action('zoom_to_100pct').trigger)
        self.canvasOptions.button('reset_view').setIcon(self.app.action('zoom_to_100pct').icon())


        # DIALOG CONSTRUCTION
        self.colorSelectorParent = self.app.action('show_color_selector').parentWidget().parentWidget()
        self.colorSelector = colorSelectorHolder()
        self.colorSelector.setWidget(self.app.action('show_color_selector').parentWidget())

        self.mainPanel.layout().addWidget(self.panelButtons)
        self.mainPanel.layout().addWidget(self.brushProperties)
        self.mainPanel.layout().addWidget(self.canvasOptions)

        self.mainWidget.addPanel('main', self.mainPanel)
        self.mainWidget.addPanel('presets', self.presetChooser)
        self.mainWidget.addPanel('color', self.colorSelector)
        self.mainWidget.addPanel('layers', self.layerList)


    def launch(self):
        self.brushProperties.slider('opacity').setValue(self.view.paintingOpacity()*100)
        self.brushProperties.slider('size').setValue(self.view.brushSize())

        self.show()
        self.activateWindow()
        self.exec_()
    
    def boop(self, text):
        msg = QMessageBox()
        msg.setText(str(text))
        msg.exec_()

    def setPreset(self, preset=None):
        if preset: 
            self.view.activateResource(self.presetChooser.currentPreset())
            self.brushProperties.slider('opacity').setValue(self.view.paintingOpacity()*100)
            self.brushProperties.slider('size').setValue(self.view.brushSize())

        self.mainWidget.setCurrentIndex(0)

    def closeEvent(self, e):
        self.colorSelector.widget().setParent(self.colorSelectorParent) # Return to previous parent is else it gets deleted?
        super().closeEvent(e)


        

    