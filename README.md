# KanvasBuddy 0.4.1
A minimalist toolbar for Krita 

![KB Main](https://github.com/Kapyia/KanvasBuddy/blob/master/images/main_panel.png)

## What is KanvasBuddy?
KanvasBuddy is a Python plugin made for Krita, a free professional and open-source painting program. KB is a small dialog that floats on top of the canvas packed with enough features to let you spend as much time in Canvas-Only mode as possible. The idea behind KB was to provide the 20% of tools used 80% of the time in the most out-of-the-way GUI possible. Its features are very similar to that of Krita's own Pop-Up Palette, but tries to be more space efficient by showing features more selectively.

KanvasBuddy features:

- A wide selection of Krita's dockers. Right there when you want them, then hidden away when not in use!
- Slider controls for the opacity, size and flow of brush presets. Specific values can also be entered by simply typing.
- Quick buttons for toggling Canvas-Only Mode, Mirror Canvas and Reset Zoom, and more.
<table>
  <tr>
    <td><img src="https://github.com/Kapyia/KanvasBuddy/blob/master/images/main_panel.png" alt="KB Main" width="100"></td>
    <td><img src="https://github.com/Kapyia/KanvasBuddy/blob/master/images/real_size.png" alt="Size Comparison" width="100"></td>
    <td><img src="https://github.com/Kapyia/KanvasBuddy/blob/master/images/maxed_out.png" alt="Maxed Out" width="100"></td>
  </tr>
</table>

## New in version 0.4.1
+ This is mainly a small patch to ensure compatibility with newer versions of Krita. The developers patched a bug in the Krita API and KanvasBuddy follows suit!
+ Pinned Panel Mode: prevent KanvasBuddy from switching back to the main panel even if you click on Krita's canvas. Enable this by clicking the tiny thumbtack in the title bar. (Credit to nickgeneratorfailed over at Krita-Artists for the suggestion)

## Who is KanvasBuddy for?
KB is best suited to someone who's already well-versed in Krita's shortcut commands. The plugin isn't meant to replace the entirety of Krita's UI, just the most essential features needed to be able to work in Canvas-Only mode.

## Download & Installation

#### Downloads:
+ **[ZIP ARCHIVE](https://github.com/Kapyia/KanvasBuddy/raw/master/KanvasBuddy-0-4-1.zip)**
+ **[SOURCE](https://github.com/Kapyia/KanvasBuddy)**

Open the **KanvasBuddy-0-4-1.zip** archive and place the **kanvasbuddy.desktop** file and the **kanvasbuddy** (all lower  case) folder in the **pykrita** directory, et voilà! Installed!
Alternatively, open Krita and go to **Tools** -> **Scripts** -> **Import Python Plugins...** and select the **KanvasBuddy-0-4-1.zip** archive and let the software handle it.

To enable KB go to **Settings** -> **Configure Krita...** -> **Python Plugin Manager** and click the checkbox to the left of the field that says **KanvasBuddy**. When you want to launch KB, simply go to **Tools** -> **Scripts** and select **KanvasBuddy**. Please note that KanvasBuddy requires you to have an open document to work.

If you want to assign a keyboard shortcut to launch KB you need to download **[kanvasbuddy.action](https://github.com/Kapyia/KanvasBuddy/raw/master/kanvasbuddy.action)**. Go to your resource directory (In Krita, go to Settings > Manage Resources… > Open Resource Folder) and create a folder called **actions**. Place the **kanvasbuddy.action** file in the newly created **actions** folder and restart Krita. You should now be able to find KanvasBuddy in the shortcut list when you go to **Settings** -> **Configure Krita...** -> **Keyboard Shortcuts**.

Happy painting! :)

## Known issues
- KB can't borrow the Tool Options docker if it's set to be in Krita's tool bar.
- People have experienced issues with the plugin on Linux. I have personally tested the plugin on several distros (Manjaro, elementary, Fedora, to name a few) without any issues, and so it's been hard for me to do any troubleshooting. I'm eager to hear from anyone who experienced issues and was able to come up with fixes for them! 
- KB features virtually no crash handling. Should KB crash you might need to restart Krita in order for KB to work again.
- Sliders and values doesn't synchronize properly between KB and Krita due to limitations in the API. This is only a visual error and does not affect functionality. 

Disclaimer: this plugin has been developed by someone better described as a 'code bodger' rather than a programmer. **Beware of spaghetti.** The plugin works well for me personally, but unfortunately I can't guarantee it'll work well for people on other systems or machines.

## License

#### KanvasBuddy is released under the GNU General Public License (version 3 or any later version).

KanvasBuddy is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

KanvasBuddy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should receive a copy of the GNU General Public License along with KanvasBuddy. If not, see <https://www.gnu.org/licenses/>.


Long story short: you're free to download, modify as well as redistribute KB as long as this ability is preserved and you give contributors proper credit. This is the same license under which Krita is released, ensuring compatibility between the two.

