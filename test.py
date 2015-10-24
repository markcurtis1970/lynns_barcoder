# For the testing

import sys
import os
from db_comms import connect, disconnect, exec_read, exec_write

connect()
exec_write("insert into items values ('val1', 'val1')")
exec_write("insert into items values ('val2', 'val2')")
exec_write("insert into items values ('val3', 'val3')")
exec_write("insert into items values ('val4', 'val4')")
exec_write("insert into items values ('val5', 'val5')")
exec_write("insert into items values ('val6', 'val6')")
exec_write("insert into items values ('val7', 'val7')")
results = exec_read("select * from items")
for result in results:
    print result
disconnect()
