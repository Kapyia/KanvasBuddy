# The KanvasBuddy Krita plugin is licensed under CC BY-NC-SA 4.0

# You are free to:
# Share — copy and redistribute the material in any medium or format
# Adapt — remix, transform, and build upon the material

# Under the following terms:
# Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
# NonCommercial — You may not use the material for commercial purposes.
# ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
# No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

from krita import PresetChooser

class KBPresetChooser(PresetChooser):

    def __init__(self, parent=None):
        super(KBPresetChooser, self).__init__(parent)
        # Remove buttons deemed excessive for this plugin
        self.layout().itemAt(0).widget().layout().itemAt(4).removeItem(self.layout().itemAt(0).widget().layout().itemAt(4).itemAtPosition(0,0))
        self.layout().itemAt(0).widget().layout().itemAt(4).removeItem(self.layout().itemAt(0).widget().layout().itemAt(4).itemAtPosition(0,1))
        self.layout().itemAt(0).widget().layout().removeItem(self.layout().itemAt(0).widget().layout().itemAt(4))


