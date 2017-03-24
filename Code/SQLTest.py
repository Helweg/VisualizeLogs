from sqlalchemy import create_engine
import socket
import time

logID = "'131'"
logDate = "'2017-03-22'"
logTime = "'08:21:43'"
logName = "'srxA-2'"
logType = "'sshd[12863]'"
logMessage = "'Accepted password for root from 10.210.14.177 port 53812 ssh2'"
logIP = "'172.210.14.131'"

engine = create_engine('postgresql://postgres:postgres@localhost:5432/Test')
connection = engine.connect()
#connection.execute("INSERT INTO logdatabase VALUES("+logDate+","+logTime+","+logName+","+logType+","+logMessage+','+logIP+")")
result = connection.execute("SELECT * FROM logdatabase")
for row in result:
    print('IP:', row['deviceip'], 'Date:', row['date'],"Time:",row['time'],'Device name:',row['devicename'],'Type:',row['type'],'Message:',row['message'])
connection.execute("DELETE FROM logdatabase")
connection.close()