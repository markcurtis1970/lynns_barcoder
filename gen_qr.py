# For the QR generation part of the barcode reader
# depends on qrencode, make sure its installed!

import sys
import os

def make_code(code):
    mycode = code
    myfile = code + ".png"
    print mycode, myfile
    os.system("qrencode -o "+ myfile + " " + mycode)
