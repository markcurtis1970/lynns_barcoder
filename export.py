# For providing data export

import sys
import os
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('bc.properties')
filepath = config.get('export','export.path')
filename = config.get('export','export.name')
filetype = config.get('export','export.type')
file = str(filepath + '/' + filename)

# export records to csv format
def exportCsv(lines):
    # some code here to write csv files
    print ""

# export to fixed width
def exportFixedWith(lines):
    # some code here to write fixed width files
    print ""

# open file for writing
def writeToFile(file,lines):
    with open (file, 'w') as expfile:
        for line in lines:
            print line
            expfile.write(str(line))
    expfile.close

def export(lines):
    # some code here for switching format
    # perhaps a select case?
    writeToFile(file, lines)

