# Script listens to serial port and writes contents to file
# requires pySerial to be installed

import serial, os, time, csv, keyboard
from pathlib import Path



# Serial port initialization (Use specific to your OS)
serialPort = '/dev/ttyUSB0'
baudRate = 9600
line = ''
ser = serial.Serial(serialPort, baudRate, timeout=3)


# Output setup
fileType = ".txt"
dataFolder = Path("/home/bertr/Documents/arduino/pintle")
fileNum = 0

for thisEntry in os.listdir(dataFolder):
    if fileType in thisEntry:
        fileNum += 1
        
currTime = time.gmtime()
fileToOpen = dataFolder / ("pintleTestRun-" + str(currTime.tm_year) + "-" + str(currTime.tm_mon) + "-" + str(currTime.tm_mday) + "_" + str(fileNum) + fileType)
outputFile = open(fileToOpen, "w+")
sensorList = "time"

try:
    line = ser.readline()
    line = line.decode('utf-8')
    x = [x.strip() for x in line.split(",")]

    for thisSensor in x:
        if x.index(thisSensor) == len(x) - 1:
            sensorList += "," + "flowMeter"
        else:
            sensorList += "," + "pxd" + str(x.index(thisSensor))

except:
    print('exception')

print(sensorList)
outputFile.write(sensorList + "\n")



while True:
    line = ser.readline()
    line = line.decode("utf-8")
    outputFile.write(str(round(time.time() * 1000)) + ',' + line)
    if keyboard.is_pressed('q'):
        break
    else:
        pass

outputFile.close()
ser.close()
