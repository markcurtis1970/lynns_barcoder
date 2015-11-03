# For the QR generation part of the barcode reader
# depends on qrencode to be installed

import sys
import os

def make_code(code):
    mycode = code
    myfile = code + ".ps"
    # using the following command format
    # barcode -e 128 -b "Hello World!" -o barcode.ps
    os.system("barcode -e 128"  + " -b '" + mycode + "' -o " + "'" + myfile + "'")
