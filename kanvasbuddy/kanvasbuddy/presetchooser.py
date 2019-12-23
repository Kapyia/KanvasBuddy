# This file is part of KanvasBuddy.

# KanvasBuddy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <https://www.gnu.org/licenses/>.

from krita import PresetChooser

class KBPresetChooser(PresetChooser):

    def __init__(self, parent=None):
        super(KBPresetChooser, self).__init__(parent)
        # Remove buttons deemed excessive for this plugin
        self.layout().itemAt(0).widget().layout().itemAt(4).removeItem(self.layout().itemAt(0).widget().layout().itemAt(4).itemAtPosition(0,0))
        self.layout().itemAt(0).widget().layout().itemAt(4).removeItem(self.layout().itemAt(0).widget().layout().itemAt(4).itemAtPosition(0,1))
        self.layout().itemAt(0).widget().layout().removeItem(self.layout().itemAt(0).widget().layout().itemAt(4))


