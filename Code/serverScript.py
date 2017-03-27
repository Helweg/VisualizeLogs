from sqlalchemy import create_engine
import socket
import time
import timestring
import paramiko
from paramiko import SSHClient
from scp import SCPClient
import sys

def main(argv):

	#mySSH = SSHConnection(sys.argv[1],sys.argv[2],sys.argv[3])
	#mySSH.getFile(sys.argv[4], sys.argv[5])
	mySplitter = Splitter(sys.argv[1], sys.argv[2])
	mySplitter.logSplit()

class Splitter:
	def __init__(self, ip, logFile):
		self.logFile = open(logFile,'r')
		self.ip = str(ip)

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
					mySQL = SQLserver(logDate, logTime, logDeviceName, logType, logMessage, self.ip)
					mySQL.insertToDB()

			elif logType == "last":
				while int(log[7]) > 0:
					log[7] = str(int(log[7])-1)
					mySQL = SQLserver(logDate, logTime, logDeviceName, logType, logMessage, self.ip)
					mySQL.insertToDB()
			else:
				logMessage = ' '.join(log[5:])
				mySQL = SQLserver(logDate, logTime, logDeviceName, logType, logMessage, self.ip)
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

class SSHConnection:
	"""docstring for SCPConnection"""
	def __init__(self, ip, uName, uPass):
		self.ssh = SSHClient()
		self.ssh.load_system_host_keys()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.connect(hostname=ip, port=22, username=uName, password=uPass)

	def getFile(self, srcDir, dstDir):
		self.scp = SCPClient(self.ssh.get_transport())

		self.scp.get(srcDir, dstDir)

		self.scp.close()


if __name__ == "__main__":
   main(sys.argv[1:])