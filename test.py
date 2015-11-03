# For the testing

import sys
import os
from db_comms import connect, disconnect, exec_read, exec_write
from export import export
import ConfigParser

connect()
exec_write("insert into items values ('PC001', 'Descr001','Make1','Model1','Serial1','Date1','Store1')")
exec_write("insert into items values ('PC002', 'Descr002','Make2','Model2','Serial2','Date2','Store2')")
exec_write("insert into items values ('PC001', 'Descr003','Make3','Model3','Serial3','Date3','Store3')")
results = exec_read("select * from items")
disconnect()

print results
for line in results:
    print line[0], line[1]

'''
print "export test..."
export(results)
'''
