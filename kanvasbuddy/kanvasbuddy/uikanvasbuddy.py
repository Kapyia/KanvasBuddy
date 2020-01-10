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

import importlib, json, os
from krita import Krita
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QSize, Qt, QEvent
from configparser import ConfigParser

from . import (
    kbsliderbox as sldbox, 
    kbbuttonbox as btnbox, 
    kbtitlebar as title,
    presetchooser as prechooser,
    kbcolorselectorframe as clrsel,
    kbpanelstack as pnlstk
)  

def boop(text): # Print a message to a dialog box
    msg = QMessageBox()
    msg.setText(str(text))
    msg.exec_()


class UIKanvasBuddy(QWidget):

    def __init__(self, kbuddy):
        super(UIKanvasBuddy, self).__init__(Krita.instance().activeWindow().qwindow())
        # -- FOR TESTING ONLY --
        importlib.reload(sldbox)
        importlib.reload(btnbox)
        importlib.reload(title)
        importlib.reload(prechooser)
        importlib.reload(pnlstk)

        self.SLIDERS = {
            'canvasRotation': sldbox.KBRotationSlider,
            'brushOpacity': sldbox.KBOpacitySlider,
            'brushFlow': sldbox.KBFlowSlider,
            'brushSize': sldbox.KBSizeSlider
        } 

        self.fileDir = os.path.dirname(os.path.realpath(__file__))
        
        self.app = Krita.instance()
        self.view = self.app.activeWindow().activeView()
        self.qwindow = self.app.activeWindow().qwindow()
        self.kbuddy = kbuddy
        self.setWindowFlags(
            Qt.Tool | 
            Qt.FramelessWindowHint
            )
        
        self.panelParents = {}

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)
        
        self.mainWidget = pnlstk.KBPanelStack(self)
        
        self.layout().addWidget(title.KBTitleBar(self))
        self.layout().addWidget(self.mainWidget)
        
        # PANEL: MAIN
        self.mainPanel = QWidget(self)
        self.mainPanel.setLayout(QVBoxLayout())
        self.mainPanel.layout().setContentsMargins(4, 4, 4, 4)

        self.mainWidget.addPanel('main', self.mainPanel)

        # PANELS
        self.panelButtons = btnbox.KBButtonBox(32) 

        # Retreive data from json
        data = None
        with open(self.fileDir + '/data.json') as jsonFile:
            data = json.load(jsonFile)
        
        # Read which widgets to enable
        config = ConfigParser()
        config.optionxform = str # Prevents ConfigParser from turning all entrys lowercase 
        config.read(self.fileDir + '/config.ini')
        

        for entry in config['PANELS']:
            if config['PANELS'].getboolean(entry):
                self.panelParents[entry] = self.qwindow.findChild(
                    QWidget, data['panels'][entry]['objectName']
                    )
                self.mainWidget.addPanel(entry, self.panelParents[entry].widget())

                # Add a button for each panel
                self.panelButtons.addButton(entry)
                self.panelButtons.button(entry).setIcon(
                    self.app.icon(data['panels'][entry]['icon'])
                    )
                self.panelButtons.button(entry).clicked.connect(
                    self.mainWidget.panel(entry).activate
                    )


        # PRESET PROPERTIES
        self.brushProperties = sldbox.KBSliderBox(self)

        for entry in config['SLIDERS']:
            if config['SLIDERS'].getboolean(entry):
                self.brushProperties.addReadySlider(entry, self.SLIDERS[entry]())


        # CANVAS OPTIONS
        self.canvasOptions = btnbox.KBButtonBox(16)

        for entry in config['CANVAS']:
            if config['CANVAS'].getboolean(entry):
                self.canvasOptions.addButton(entry)
                self.canvasOptions.button(entry).clicked.connect(
                    self.app.action(data['canvasOptions'][entry]['action']).trigger
                    )
                self.canvasOptions.button(entry).setIcon(
                    self.app.icon(data['canvasOptions'][entry]['icon'])
                    )


        # MAIN DIALOG CONSTRUCTION
        self.mainPanel.layout().addWidget(self.panelButtons)
        self.mainPanel.layout().addWidget(self.brushProperties)
        self.mainPanel.layout().addWidget(self.canvasOptions)

    def launch(self):
        self.brushProperties.synchronizeSliders()
        self.show()


    def setPreset(self, preset=None):
        if preset: 
            self.view.activateResource(self.presetChooser.currentPreset())
            self.brushProperties.slider('opacity').setValue(self.view.paintingOpacity()*100)
            self.brushProperties.slider('size').setValue(self.view.brushSize())

        self.mainWidget.setCurrentIndex(0)


    def closeEvent(self, e):
        # Return borrowed widgets to previous parents or else we're doomed
        for parent in self.panelParents:
            self.panelParents[parent].setWidget(self.mainWidget.panel(parent).widget())
            self.panelParents[parent].widget().setEnabled(True)

        # self.colorSelectorParent.setWidget(self.colorSelector.widget()) 
        # self.layerBoxParent.setWidget(self.layerBox)
        self.kbuddy.setIsActive(False)
        super().closeEvent(e)


    def mousePressEvent(self, e):
        self.setFocus()    