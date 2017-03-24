from sqlalchemy import create_engine
import socket
import time
import timestring

class Splitter:
	def __init__(self):
		self.logFile = open('testMessage','r')

	def logSplit(self):
		for log in self.logFile:
			log = log.replace("'","´")
			log = log.split()
			logDate = str(timestring.Date(' '.join(log[0:2])))[0:10]
			logTime = log[2]
			logDeviceName = log[3]
			logType = log[4]

			if logType[-1:] != ":":
					logType = "Null"
					logMessage = ' '.join(log[4:])
					mySQL = SQLserver(logDate, logTime, logDeviceName, logType, logMessage, '172.210.14.131')
					mySQL.insertToDB()

			elif logType == "last":
				while int(log[7]) > 0:
					log[7] = str(int(log[7])-1)
					mySQL = SQLserver(logDate, logTime, logDeviceName, logType, logMessage, "172.210.14.131")
					mySQL.insertToDB()
			else:
				logMessage = ' '.join(log[5:])
				mySQL = SQLserver(logDate, logTime, logDeviceName, logType, logMessage, "172.210.14.131")
				mySQL.insertToDB()

		self.logFile.close()

class SQLserver(object):
	def __init__(self, logDate, logTime, logDeviceName, logType, logMessage, logIP):
		self.engine = create_engine('postgresql://postgres:postgres@localhost:5432/Test')
		self.connection = self.engine.connect()
		self.logDate = "'"+logDate+"'"
		self.logTime = "'"+logTime+"'"
		self.logDeviceName = "'"+logDeviceName+"'"
		self.logType = "'"+logType+"'"
		self.logMessage = "'"+logMessage+"'"
		self.logIP = "'"+logIP+"'"

	def insertToDB(self):
		self.connection.execute("INSERT INTO logdatabase VALUES("+self.logDate+","+self.logTime+","+self.logDeviceName+","+self.logType+","+self.logMessage+','+self.logIP+")")
		self.connection.close()		

mySplitter = Splitter()
mySplitter.logSplit()
