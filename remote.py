#! /usr/bin/env python3
# send jvc ccu RM-P210 commands
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, parity=serial.PARITY_EVEN)
ser.timeout=0.1

connected=False
while(not connected):
    ser.write(64)
    if(ser.read()==0x80):
        ser.write(0xA0)
        connected=True
        print("connected")
    else:
        print("waiting")
    time.sleep(0.8)

while(True):
    ser.write(0x83)
    ser.read()
    ser.write([64,7,72])
    ser.read()
    time.sleep(2)

    ser.write(0x83)
    ser.read()
    ser.write([65,7,72])
    ser.read()
    time.sleep(2)

    ser.write(0x83)
    ser.read()
    ser.write([66,7,72])
    ser.read()
    time.sleep(2)
