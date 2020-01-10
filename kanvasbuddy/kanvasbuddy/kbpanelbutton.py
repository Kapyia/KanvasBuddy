from krita import Krita

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QToolButton
from PyQt5.QtGui import QIcon, QPixmap, QImage, QColor
from PyQt5.QtCore import QSize, Qt

APP = Krita.instance()
CANVAS = APP.activeWindow().activeView().canvas()

class KBButton(QToolButton):

    def __init__(self, size):
        super(KBButton, self).__init__()
        self.setFixedSize(QSize(size, size))
    
    def setIcon(self, icon):
        if isinstance(icon, QIcon):
            super().setIcon(icon)
        elif isinstance(icon, QPixmap):
            super().setIcon(QIcon(icon))
        elif isinstance(icon, QImage):
            super().setIcon(QIcon(QPixmap.fromImage(icon)))
        else:
            raise TypeError(f"Unable to set icon of invalid type {type(icon)}")

    def setColor(self, color): # In case the Krita API opens up for a "color changed" signal, this could be useful...
        if isinstance(color, QColor):
            pxmap = QPixmap(self.iconSize())
            pxmap.fill(color)
            self.setIcon(pxmap)
        else:
            raise TypeError(f"Unable to set color of invalid type {type(color)}")


class KBPresetChooserButton(KBButton):

    def __init__(self, size):
        super(KBPresetChooserButton, self).__init__()
        self.setIcon(APP.icon('light_paintop_settings_01'))
        self.clicked.connect()


class KBColorPickerButton(KBButton):

    def __init__(self, size):
        super(KBColorPickerButton, self).__init__()
        self.setIcon(APP.icon('light_krita_tool_color_picker'))


class KBLayersButton(KBButton):

    def __init__(self, size):
        super(KBLayersButton, self).__init__()
        self.setIcon(APP.icon('light_duplicatelayer'))


class KBToolOptionsButton(KBButton):

    def __init__(self, size):
        super(KBToolOptionsButton, self).__init__()
        self.setIcon(APP.icon('light_paintop_settings_02'))


class KBCanvasOnlyButton(KBButton):

    def __init__(self, size):
        super(KBCanvasOnlyButton, self).__init__()
        action = APP.action('view_show_canvas_only')
        self.setIcon(action.icon())
        self.clicked.connect(
            lambda: 
                action.trigger
            )
class KBMirrorButton(KBButton):

    def __init__(self, size):
        super(KBMirrorButton, self).__init__()
        action = APP.action('mirror_canvas')
        self.setIcon(action.icon())
        self.clicked.connect(
            lambda: 
                action.trigger
            )

class KBResetZoomButton(KBButton):

    def __init__(self, size):
        super(KBResetZoomButton, self).__init__()
        action = APP.action('zoom_to_100pct')
        self.setIcon(action.icon())
        self.clicked.connect(
            lambda: 
                action.trigger
            )
