#! /usr/bin/env python3
# send jvc ccu RM-P210 commands
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, parity=serial.PARITY_EVEN)
ser.timeout=0.1

def waitCam():
    r=ser.read()
    if(r == b'\xA0'):
        print("cam accept")
    else:
        print("cam reject")

def sendCmd(cmd):
    ser.write(b'\x83')
    waitCam()
    ser.write(cmd)
    waitCam()

def sendVal(cmd):
    ser.write(b'\x84')
    waitCam()
    ser.write(cmd)
    waitCam()

connected=False
while(not connected):
    ser.write(b'\x80')
    r=ser.read()
    print(r)
    if(r == b'\x80'):
        ser.write(b'\xA0')
        connected=True
        print("connected")
    else:
        print("waiting")
    time.sleep(0.8)

sendCmd(b'\x41\x7D\x3E')
sendCmd(b'\x40\x00\x40')
sendCmd(b'\x41\x51\x12')
sendCmd(b'\x42\x03\x45')
sendCmd(b'\x40\x02\x42')
sendVal(b'\x00\x06\x44\x4A')
sendCmd(b'\x41\x02\x43')
sendVal(b'\x04\x06\x44\x4E')
sendCmd(b'\x41\x02\x43')
sendCmd(b'\x61\x06\x67')
sendCmd(b'\x41\x03\x44')
sendCmd(b'\x40\x0C\x4C')
sendCmd(b'\x41\x0C\x4D')
sendCmd(b'\x42\x0C\x4E')
sendCmd(b'\x43\x0C\x4F')
sendCmd(b'\x44\x0C\x50')
sendCmd(b'\x45\x0C\x51')
sendCmd(b'\x46\x0C\x52')
sendCmd(b'\x4F\x0C\x5B')
sendVal(b'\x05\x62\x6E\x55')
sendCmd(b'\x40\x0C\x4C')
sendVal(b'\x00\x64\x14\x78')

time.sleep(1)
ser.write(0x83)
ser.read()
ser.write([65,7,72])
ser.read()
time.sleep(2)

#ser.write(0x83)
#ser.read()
#ser.write([66,7,72])
#ser.read()
#time.sleep(2)
