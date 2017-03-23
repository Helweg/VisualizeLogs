import timestring

log = "Mar 22 08:21:43  srxA-2 sshd[12863]: Accepted password for root from 10.210.14.177 port 53812 ssh2"
log = log.split()
print (log)
logDate = str(timestring.Date(' '.join(log[0:2])))[0:10]
logTime = log[2]
logDeviceName = log[3]
logType = log[4]
logMessage = ' '.join(log[5:])
print (logDate)
print (logTime)
print (logDeviceName)
print (logType)
print (str(logMessage))