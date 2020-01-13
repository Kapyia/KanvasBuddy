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
- other KB-Widgets also create sub-widgets from dictionaries (if possible)
'''


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

        self.fileDir = os.path.dirname(os.path.realpath(__file__))
        
        self.app = Krita.instance()
        self.view = self.app.activeWindow().activeView()
        self.kbuddy = kbuddy
        self.setWindowFlags(
            Qt.Tool | 
            Qt.FramelessWindowHint
            )

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)
        
        self.panelStack = pnlstk.KBPanelStack(self)
        
        self.layout().addWidget(title.KBTitleBar(self))
        self.layout().addWidget(self.panelStack)

        config = self.loadConfig()
        jsonData = self.loadJSON()

        # SET UP PANELS
        for entry in config['PANELS']:
            if config['PANELS'].getboolean(entry):
                # if entry == 'presetChooser':
                #   add custom preset chooser 
                self.panelStack.loadPanel(jsonData['panels'][entry])


        # SET UP PRESET PROPERTIES
        self.brushProperties = sldbox.KBSliderBar(self)

        for entry in config['SLIDERS']:
            if config['SLIDERS'].getboolean(entry):
                self.brushProperties.addSlider(entry)

        self.panelStack.main().layout().addWidget(self.brushProperties)


        # SET UP CANVAS OPTIONS
        self.canvasOptions = btnbox.KBButtonBar(16)

        for entry in config['CANVAS']:
            if config['CANVAS'].getboolean(entry):
                self.canvasOptions.loadButton(
                    jsonData['canvasOptions'][entry],
                    self.app.action(jsonData['canvasOptions'][entry]['id']).trigger
                    )

        self.panelStack.main().layout().addWidget(self.canvasOptions)


    def loadJSON(self):
        try:
            with open(self.fileDir + '/data.json') as jsonFile:
                data = json.load(jsonFile)
                return data
        except:
            boop("Error: Failed to load JASON data")
            self.close()


    def loadConfig(self):
        try:
            cfg = ConfigParser()
            cfg.optionxform = str # Prevents ConfigParser from turning all entrys lowercase 
            cfg.read(self.fileDir + '/config.ini')
            return cfg
        except:
            boop("Error: Failed to load config file")
            self.close()

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