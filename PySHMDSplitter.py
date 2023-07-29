import tkinter
import binascii
import pyperclip
import math

#special thanks to stacks overflow for all this lmao
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print("Importing to: "+filename)

#again, thanks to stacks overflow kekw
try:
    with open(filename, 'r') as f: #not in binary anymore because we are using SPFA
        content = str(f.read())
except:
    print("Please choose a file.")
    quit()
#print(content)

#Delimiter
if len(content) > 536870888: #memory limit capped to a little under 1/4th of the 32 bit integer limit because scratch is weird...
    filesize = len(content)
    messagebox.showwarning("Critical Error", "Out of Memory.\n\nMaximum SPFA filesize:\n536'870'888 Bytes.\n\nCurrent SPFA filesize:\n"+ str(f"{filesize:_}").replace("_","'") + " Bytes")
    exit()

SPFAsep = "\\"

spfalist = content.split(SPFAsep)

#name and mode of MIDI
MIDIName = str(spfalist[0])
MIDIMode = str(spfalist[1])


#print(*spfalist, sep = "\n")
print(MIDIName) #MIDI Name
print(MIDIMode) #MIDI Import Mode

limiter = 6400000 * 4 #limit to 6'200'000 events, each event is composed of 4 attributes.

#prepares slicing
n_spfalist = spfalist[2:]
n_spfaslice = []
iteration = int(math.ceil(len(n_spfalist)/limiter))

if (iteration == 1):
    print("This MIDI does not need to be sliced. It can be run on Scratch.")
    #quit()
else:
    print(str(iteration) + " slices needed.")

#verifier
len_a = len(content)
len_b = 0

#splits the spfalist into slices
#does this by combining (idx-1)*limiter-th entry to the (idx*limiter)-1-th entry
#into a string then appending to the slice. it's just division
for idx in range(iteration):
    n_first = int(((idx)*limiter))
    n_last = int((((idx+1)*limiter)))
    n_spfaslice.append(SPFAsep.join(n_spfalist[n_first:n_last]))
    print(str(idx) + " | " + str(n_first) + " to " + str(n_last))
    #n_spfaslice.append(n_spfalist[int(((idx-1)*limiter)):int(((idx*limiter)-1))])
    if idx == 0:
        OutContent = MIDIName + "*" + SPFAsep + MIDIMode + SPFAsep #asterisk now indicates if it requires merging
    else:
        OutContent = SPFAsep
    OutContent = OutContent + (n_spfaslice[idx])
    OutMIDIName = "_" + MIDIName + "." + str(idx) + ".shmd"
    #i hope this works
    len_b = len_b + len(OutContent)
    print(str(len(OutContent)) + " characters long")
    print(OutContent)
    spfaslice = open(OutMIDIName, "w")
    spfaslice.write(OutContent)
    spfaslice.close()

print("Length of Primary File: " + str(len_a) + "\nLength of Split File: " + str(len_b) + "\nDifferences in Length: " + str(len_a - len_b) + "\nValue must be -1." )
if (len_a - len_b != -1):
    print("WARNING: Size Mismatch.")