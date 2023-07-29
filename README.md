# Python Converted MIDI Splitter

This series of programs developed in Python make it possible to split any large converted MIDI formats:

1. Modified Format for Eden/Ojasn MIDI Players 
2. Modified Format for Eden/Ojasn MIDI Players \[Hex Values\] (Only compatible with KazuMIDI 1.2.x, only benefit is each file takes lesser space.)
3. Aranara MIDI File Format for Aranara MIDI Player (Only compatible with said MIDI Player.)

Files are split into volumes which can then be imported to their respective MIDI Players without crashing due to memory issues.

**Note: Should the split MIDI cause memory issues, decrease the limiter variable until the split MIDI can be opened.**

## Usage:

__**The file limit is strictly set to 536MB for any converted file.**__

### Please note that the following programs are compatible with split MIDI files:

1. KazuMIDI 1.1 and later
2. Aranara MIDI Player

Take note of the converted file you are splitting:

1. For **SPFA** files, use **PySPFASplitter.py**.
2. For **SHMD** files, use **PySHMDSplitter.py**.
3. For **AraMIDI** files, use **PyAraMSplitter.py**.

Split files will output to the directory of the conversion programs.
__Drag and drop the split files upon IMPORT, but **always start with files ending in 0.SPFA/0.SHMD/0.AraMIDI!**__

The player will then merge all split files into one large file and will attempt to play.