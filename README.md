# KanvasBuddy 0.1
A minimalist toolbar plugin for Krita 

**(KB has been abandoned by it's original developer. I've hit a point where limitations to the Krita Python API and the PyQt5 bindings are giving me more frustration than joy working on the project.)**

## What is KanvasBuddy?
KanvasBuddy is a plugin made for Krita, a free professional and open-source painting program. KB is a small dialog that floats on top of the canvas and aims to let you spend as much time in Canvas-Only mode as possible without compromises. The goal of KB is to provide artists with the 20% of tools they use 80% of the time in the most out-of-the-way GUI possible. One may think of KB as an alternative take on Krita's built-in Pop-Up Palette.

KanvasBuddy 0.1 features:

- Krita's full Brush Presets list
- Krita's Advanced Color Selector (very literally) - size large!
- Brush Opacity and Size controls
- Quick buttons for Canvas-Only Mode, Mirror Canvas and Reset Zoom 

## Who is KanvasBuddy for?
To be blunt, the intended user for KB has always been myself. Catering to the needs of a single artist made it easier to keep the number of features - and thus the size of the dialog - to an absolute minimum.

KB is best suited to someone who's workflow more closely resembles that of a traditional painter and who is already well-versed in Krita's shortcuts. 

## Known issues
- KB borrows the actual Advanced Color Selector and unfortunately breaks it's resizability
- KB features virtually no crash handling and a new instance can't be opened if the plugin doesn't exit cleanly

Disclaimer: this plugin has been developed by someone better described as a 'code bodger' rather than a programmer. **Beware of the spaghetti.** The plugin works well for me personally, but I can't guarantee it'll work well for people on other systems and/or machines.

## License

#### The KanvasBuddy Krita plugin is licensed under CC BY-NC-SA 4.0

You are free to:
+ Share — copy and redistribute the material in any medium or format
+ Adapt — remix, transform, and build upon the material

Under the following terms:
+ Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
+ NonCommercial — You may not use the material for commercial purposes.
+ ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
+ No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

![CC](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png "CC BY-NC-SA 4.0")

(tl;dr one is free to download, modify and redistribute this plugin as long as it remains so)
