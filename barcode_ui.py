# For the UI part of the barcode reader

from Tkinter import *
from gen_qr import make_code

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

# make new barcode
def makebc():
    print "make barcode"
    if (myCodeEntry.get() != ""):
        make_code(myCodeEntry.get())

# *** create list and text boxes ***

# enumerate the list of attributes (number, value)
# the end value of row determines where everything
# is at the bottom
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

# the end value of row determines where everything
# is at the bottom
pos1 = i + 1
pos2 = i + 2
pos3 = i + 3

# *** create new box for new code ***
myCodeLabel = Label(root, text = "Enter barcode")
myCodeLabel.grid(column = 0, row = pos2)
myCodeEntry = Entry(root)
myCodeEntry.grid(column = 1, row = pos2)

# *** create buttons ***

myRead = Button ( root, command = read, text = "read from db")
myRead.grid(column = 0, row = pos1)
myWrite = Button ( root, command = write, text = "write to db")
myWrite.grid(column = 1, row = pos1)
myMakebc = Button ( root, command = makebc, text = "make code")
myMakebc.grid(column = 0, row = pos3)

root.mainloop()
