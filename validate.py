# For providing validation
# if required

import sys
import os
from db_comms import connect, disconnect, exec_read, exec_write
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('bc.properties')

# checks all properties are present
def checkProperties():
    
