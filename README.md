# KanvasBuddy 0.3
A minimalist toolbar for Krita 

![KB Main](https://github.com/Kapyia/KanvasBuddy/blob/master/images/main_panel.png)

## What is KanvasBuddy?
KanvasBuddy is a Python plugin made for Krita, a free professional and open-source painting program. KB is a small dialog that floats on top of the canvas packed with enough features to let you spend as much time in Canvas-Only mode as possible. The idea behind KB was to provide the 20% of tools used 80% of the time in the most out-of-the-way GUI possible. Its features are very similar to that of Krita's own Pop-Up Palette, but tries to be more space efficient by showing features more selectively.

KanvasBuddy features:

- Krita's full Brush Presets list
- Krita's Advanced Color Selector - size large!
- Krita's Layers Docker
- Brush Opacity and Size controls
- Quick buttons for Canvas-Only Mode, Mirror Canvas and Reset Zoom 
<table>
  <tr>
    <td><img src="https://github.com/Kapyia/KanvasBuddy/blob/master/images/main_panel.png" alt="KB Main" width="100"></td>
    <td><img src="https://github.com/Kapyia/KanvasBuddy/blob/master/images/advanced_color_selector.png" alt="Advanced Color Selector" width="100"></td>
    <td><img src="https://github.com/Kapyia/KanvasBuddy/blob/master/images/brush_preset_list.png" alt="Brush Presets" width="100"></td>
    <td><img src="https://github.com/Kapyia/KanvasBuddy/blob/master/images/real_size.png" alt="Size Comparison" width="100"></td>
  </tr>
</table>

## New in version 0.3
+ Shortcut commands should no longer be gobbled up by KB  
+ The close button won't be triggered by pressing the space bar anymore, pan the canvas in peace!
+ As the creator of and sole contributor to KB I've decided to, as of version 0.3, switch the license of KB from CC BY-NC-SA 4.0 to GNU GPL. It changes virtually nothing about how open KB is to the users but means that KB and Krita will be released under the same license. The switch just makes sense to me.
+ Bonus: the source now features a small diagram over how KB is constructed.

## Who is KanvasBuddy for?
To be blunt, the intended user for KB has always been myself. Catering to the need of a single artist made it easier to keep the number of features - and thus the size of the dialog - to an absolute minimum. That being said, feedback is welcomed but I also encourage people to tinker with the script to adapt it to their own needs.

KB is best suited to someone who's workflow more closely resembles that of a traditional painter and who is already well-versed in Krita's shortcut commands. 

## Download & Installation

#### Downloads:
+ **[ZIP ARCHIVE](https://drive.google.com/file/d/1QRMH3b2OsjButrI-MlzlGV4qA2u-c0t6/view?usp=sharing)**
+ **[SOURCE](https://github.com/Kapyia/KanvasBuddy)**

Open the **kanvasbuddy-0-3.zip** archive and place the **kanvasbuddy.desktop** file and the **kanvasbuddy** (all lower  case) folder in the **pykrita** directory, et voilà! Installed!
Alternatively, open Krita and go to **Tools** -> **Scripts** -> **Import Python Plugins...** and select the **kanvasbuddy-0-3.zip** archive and let the software handle it.

To enable KB go to **Settings** -> **Configure Krita...** -> **Python Plugin Manager** and click the checkbox to the left of the field that says **KanvasBuddy**. When you want to launch KB, simply go to **Tools** -> **Scripts** and select **KanvasBuddy**. Please note that KanvasBuddy requires you to have an open document to work.

Happy painting! :)

## Known issues
- Issues on Linux based operating systems are being looked into, so please provide any information you have on them! Linux doesn't love my sets of hardware, but I'll do my best to work them out.
- KB features virtually no crash handling. Should KB crash you might need to restart Krita in order for KB to work again.
- Sliders and values doesn't synchronize properly between KB and Krita due to limitations in the API. This is only a visual error and does not affect functionality. 

Disclaimer: this plugin has been developed by someone better described as a 'code bodger' rather than a programmer. **Beware of spaghetti.** The plugin works well for me personally, but unfortunately I can't guarantee it'll work well for people on other systems and/or machines.

## License

#### KanvasBuddy is released under the GNU General Public License (version 3 or any later version).

KanvasBuddy is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

KanvasBuddy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should receive a copy of the GNU General Public License along with KanvasBuddy. If not, see <https://www.gnu.org/licenses/>.


Long story short: you're free to download, modify as well as redistribute KB as long as this ability is preserved and you give contributors proper credit. This is the same license under which Krita is released, ensuring compatibility between the two.

