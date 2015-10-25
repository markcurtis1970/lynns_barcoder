# For the DB part of the barcode reader

import sys
import os
import sqlite3 as mydb
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('bc.properties')
dbname = config.get('db','db.name')

con = None

# *** connect to the db ***
def connect():
    global con
    try:    
        con = mydb.connect(dbname)

    except mydb.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    return con

# execute a read from the db
def exec_read(statement):
    
    try: 
        cur = con.cursor()
        cur.execute(statement)
        rows = cur.fetchall()
    except mydb.Error, e:
        print "Error %s:" % e.args[0]
    return rows

# execute a write to the db
def exec_write(statement):
    
    try:
        cur = con.cursor()
        cur.execute(statement)
        con.commit()
    except mydb.Error, e:
        print "Error %s:" % e.args[0]

# disconnect from the db
def disconnect():

    if con:
        con.close()
