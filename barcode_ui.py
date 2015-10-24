# For the UI part of the barcode reader

from Tkinter import *
import random

# Setup variables
root = Tk()
attributes = sys.argv
entries = []
labels = []

# *** Functions ***

# check there is a barcode before reading
def checkCode():
    if (entries[0].get() == ""):
        print "no entry"
    else:
        print entries[0].get()

# read from the data source
def read ():
    print "read command"
    checkCode();

# write to the data source
def write ():
    print "write command"

# *** create list and text boxes ***

# enumerate the list of attributes (number, value)
for i,a in enumerate(attributes):
    # exclude the first item which is the file name
    if i > 0 :
        myLabel = Label(root, text = a)
        myLabel.grid(column = 0, row = i)
        labels.append(myLabel)
        myEntry = Entry(root)
        myEntry.grid(column = 1, row = i)
        entries.append(myEntry)
        # use i-1 as we had to negate the first entry
        entries[i-1].insert(INSERT,"text to insert")

# *** create buttons ***

myRead = Button ( root, command = read, text = "Read")
myRead.grid(column = 0, row = i +1)
myWrite = Button ( root, command = write, text = "Write")
myWrite.grid(column = 1, row = i +1)

root.mainloop()
