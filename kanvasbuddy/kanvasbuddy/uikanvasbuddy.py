# The KanvasBuddy Krita plugin is licensed under CC BY-NC-SA 4.0

# You are free to:
# Share — copy and redistribute the material in any medium or format
# Adapt — remix, transform, and build upon the material

# Under the following terms:
# Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
# NonCommercial — You may not use the material for commercial purposes.
# ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
# No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

import importlib
from krita import Krita, PresetChooser
from PyQt5.QtWidgets import QWidget, QDialog, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QSize, Qt

from . import (
    kbsliderbox as sldbox, 
    kbbuttonbox as btnbox, 
    kbtitlebar as title,
    presetchooser as prechooser,
    kbcolorselectorframe as clrsel,
    kbpanelstack as pnlstk
)

class UIKanvasBuddy(QDialog):

    def __init__(self, kbuddy):
        super(UIKanvasBuddy, self).__init__(Krita.instance().activeWindow().qwindow())
        # -- FOR TESTING ONLY --
        # importlib.reload(sldbox)
        # importlib.reload(btnbox)
        # importlib.reload(title)
        # importlib.reload(prechooser)
        # importlib.reload(pnlstk)

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
        self.panelButtons.button('color').clicked.connect(lambda: self.mainWidget.setCurrentIndex(2))

        self.panelButtons.addButton('layers')
        self.panelButtons.button('layers').setIcon(self.app.icon('light_duplicatelayer'))
        self.panelButtons.button('layers').clicked.connect(lambda: self.mainWidget.setCurrentIndex(3))


        # WIDGET: PRESET CHOOSER        
        self.presetChooser = prechooser.KBPresetChooser()
        self.presetChooser.presetSelected.connect(self.setPreset)
        self.presetChooser.presetClicked.connect(self.setPreset)


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


        # MAIN DIALOG CONSTRUCTION
        self.colorSelectorParent = self.app.action('show_color_selector').parentWidget().parentWidget().parentWidget()
        self.colorSelector = clrsel.KBColorSelectorFrame(self.app.action('show_color_selector').parentWidget().parentWidget()) # Borrow the Advanced Color Selector

        self.layerBoxParent = self.app.action('help_about_app').parentWidget().findChild(QWidget, 'KisLayerBox') 
        self.layerBox = self.layerBoxParent.widget() # Borrow the Layer Docker

        self.mainPanel.layout().addWidget(self.panelButtons)
        self.mainPanel.layout().addWidget(self.brushProperties)
        self.mainPanel.layout().addWidget(self.canvasOptions)

        self.mainWidget.addPanel('main', self.mainPanel)
        self.mainWidget.addPanel('presets', self.presetChooser)
        self.mainWidget.addPanel('color', self.colorSelector)
        self.mainWidget.addPanel('layers', self.layerBox)


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
        # Return borrowed widgets to previous parents or else we're doomed
        self.colorSelectorParent.setWidget(self.colorSelector.widget()) 
        self.layerBoxParent.setWidget(self.layerBox)
        self.kbuddy.setIsActive(False)
        super().closeEvent(e)


        

    