#read data from serial port + current time

import serial
import time
import datetime

ser = serial.Serial("COM14", 115200)  # type: object

count = 0
while 1:
    if ser.inWaiting():
        x = ser.readline()
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')

        if True:
            textToWrite = st + " " + x
            print(textToWrite)
        count += 1

## close the serial connection 
ser.close()
