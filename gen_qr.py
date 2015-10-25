# For the QR generation part of the barcode reader
# depends on qrencode to be installed

import sys
import os

def make_code(code):
    mycode = code
    myfile = code + ".png"
    os.system("qrencode -o "+ myfile + " " + mycode)
