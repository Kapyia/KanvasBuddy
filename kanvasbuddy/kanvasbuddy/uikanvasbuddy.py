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

''' GAME PLAN
- the new sizeHint():
    if self.customSizeHint:
        return self.customSizeHint
    else:
        return widget.sizeHint()
'''

import importlib, json
from os import path
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

        self.fileDir = path.dirname(path.realpath(__file__))
        
        self.view = Krita.instance().activeWindow().activeView()
        self.kbuddy = kbuddy
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)
        
        self.layout().addWidget(title.KBTitleBar(self))

        # LOAD CONFIG DATA
        config = self.loadConfig()
        jsonData = self.loadJSON()
        
        # SET UP PANELS
        self.panelStack = pnlstk.KBPanelStack(self)
        self.initPanels(config['PANELS'], jsonData['panels'])
        self.layout().addWidget(self.panelStack)

        # SET UP PRESET PROPERTIES
        self.brushProperties = sldbox.KBSliderBar(self)
        self.initSliders(config['SLIDERS'])
        self.panelStack.main().layout().addWidget(self.brushProperties)

        # SET UP CANVAS OPTIONS
        self.canvasOptions = btnbox.KBButtonBar(16)
        self.initCanvasOptions(config['CANVAS'], jsonData['canvasOptions'])
        self.panelStack.main().layout().addWidget(self.canvasOptions)


    def initPanels(self, config, data):
        for entry in config:
            if config.getboolean(entry):
                self.panelStack.loadPanel(data[entry])


    def initSliders(self, config):
        for entry in config:
            if config.getboolean(entry):
                self.brushProperties.addSlider(entry)


    def initCanvasOptions(self, config, data):
        for entry in config:
            if config.getboolean(entry):
                self.canvasOptions.loadButton(
                    data[entry],
                    Krita.instance().action(data[entry]['id']).trigger
                    )


    def loadJSON(self):
        with open(self.fileDir + '/data.json') as jsonFile:
            data = json.load(jsonFile)
            return data


    def loadConfig(self):
        cfg = ConfigParser()
        cfg.optionxform = str # Prevents ConfigParser from turning all entrys lowercase 
        cfg.read(self.fileDir + '/config.ini')
        return cfg


    def launch(self):
        self.brushProperties.synchronizeSliders()
        self.panelStack.currentChanged(0)
        self.show()


    def setPreset(self, preset=None):
        if preset: 
            self.view.activateResource(self.presetChooser.currentPreset())
            self.brushProperties.slider('opacity').setValue(self.view.paintingOpacity()*100)
            self.brushProperties.slider('size').setValue(self.view.brushSize())

        self.panelStack.setCurrentIndex(0)


    def closeEvent(self, e):
        self.panelStack.dismantle() # Return borrowed widgets to previous parents or else we're doomed
        self.kbuddy.setIsActive(False)
        super().closeEvent(e)


    def mousePressEvent(self, e):
        self.setFocus()    