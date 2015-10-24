# For the UI part of the barcode reader

from Tkinter import *
import random

# Setup variables
root = Tk()
attributes = sys.argv
entries = []
labels = []

# Functions

def read ():
    print "read command"

def write ():
    print "write command"

# For testing
#attributes = {'Field1', 'Field2', 'Field3', 'Field4', 'Field5', 'Field6'}

# Generate the list and text boxes
#
# enumerate the list of attributes (number, value)
for i,a in enumerate(attributes):
    # exclude the first item which is the file name
    if i > 0 :
        myLabel = Label(root, text = a)
        myLabel.grid(column=0, row = i)
        labels.append(myLabel)
        myEntry = Entry(root)
        myEntry.grid(column=1, row=i)
        entries.append(myEntry)
        # use i-1 as we had to negate the first entry
        entries[i-1].insert(INSERT,"text to insert")

# Generate the buttons

myRead = Button ( root, command = read, text = "Read")
myRead.grid(column = 0, row = i +1)
myWrite = Button ( root, command = write, text = "Write")
myWrite.grid(column = 1, row = i +1)

root.mainloop()
