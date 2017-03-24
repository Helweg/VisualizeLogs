import timestring

logFile = open('testMessage','r')
#logFile = ["Mar 22 08:21:43  srxA-2 sshd[12863]: Accepted password for root from 10.210.14.177 port 53812 ssh2", "Mar 21 12:54:18  srxA-2 last message repeated 11 times"]
#log = "Mar 21 12:54:18  srxA-2 last message repeated 11 times"

for log in logFile:
	log = log.split()
	logDate = str(timestring.Date(' '.join(log[0:2])))[0:10]
	logTime = log[2]
	logDeviceName = log[3]

	if log[4] == "last":
		while int(log[7]) > 0:
			log[7] = str(int(log[7])-1)

			print (logDate)
			print (logTime)
			print (logDeviceName)
			print (logType)
			print (str(logMessage))

	else:
		logType = log[4]

		if logType[-1:] == ":":
			logType = "Null"
			logMessage = ' '.join(log[4:])
		else:
			logMessage = ' '.join(log[5:])


			print (logDate)
			print (logTime)
			print (logDeviceName)
			print (logType)
			print (str(logMessage))

logFile.close()