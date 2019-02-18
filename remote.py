#! /usr/bin/env python3
# send jvc ccu RM-P210 commands
import serial
import csv
import time

key_id = []
cmd_id = []

with open('cmds.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if(row[0]=="key"):
            key_id.append(row)
        if(row[0]=="cmd"):
            cmd_id.append(row)

ser = serial.Serial('/dev/ttyUSB0', 9600, parity=serial.PARITY_EVEN)
ser.timeout=0.1

await_cam = False

def waitCam():
    ack=False
    while(not ack):
        try:
            r = ord(ser.read())
#            print("cam: "+hex(r))
            ack=True
        except TypeError:
            print("waiting for CAM...")
            ack=False

    #if(r == 0xA0):
    #    print("ACK")
    #else:
    #    print("cam reject")

def SpecialTransmitt(data):
    ser.flushInput()
    print("#### Special Transmit beginn ####")
    tx=0x90|data
    ser.write(b'\x90')
    print("write: 0x90")
    waitCam()
    waitCam()
    ser.write(b'\xA0')
    print("write: 0xA0")
    waitCam()
    waitCam()
    waitCam()
    ser.write(b'\xA0')
    print("write: 0xA0")

    waitCam()
    ser.write(b'\xA0')
    print("write: 0xA0")
    waitCam()
    waitCam()
    waitCam()
    ser.write(b'\xA0')
    print("write: 0xA0")

    print("#### Special Transmit end ####")

def sendCmd(cmd, data, special=False):
    print("sendCmd "+str(cmd)+" = "+str(data))

    if(type(cmd) is str):
        found = False
        for x in cmd_id:
            if(x[5]==cmd):
                found = True
                cmd=int(x[1],0)
        if( not found ):
            print("unknown string: \""+cmd+"\"")
            exit()

    if(type(data) is str):
        found = False
        for x in cmd_id:
            if(int(x[1],0)==cmd and x[6]==data):
                found = True
                data=int(x[2],0)
        if( not found ):
            print("unknown string: \""+data+"\"")
            exit()


    tx=[data|0x40,cmd,0]
    if(special):
        tx[0]=tx[0]|0x2
    tx[2]=(tx[0]+tx[1])&0x7F

    ser.write(b'\x83')
    #time.sleep(0.003)
    waitCam()
    ser.write(tx)
    #time.sleep(0.01)
    waitCam()

def sendKey(key, val):
    print("sendKey "+str(key)+" = "+str(val))
    if(type(key) is str):
        found = False
        for x in key_id:
            if(x[5]==key):
                found = True
                key=int(x[1],0)
        if( not found ):
            print("unknown string: \""+key+"\"")
            exit()

    if(type(val) is str):
        found = False
        for x in key_id:
            if(int(x[1],0)==key and x[6]==val):
                found = True
                val=int(x[2],0)
        if( not found ):
            print("unknown string: \""+val+"\"")
            exit()

    #key = (packet[0] << 4) | ((packet[1] & 0xF0) >> 4)
    #val = ((packet[1] & 0x0F) << 8) | packet[2]
    tx = [ ((key&0xFF0) >> 4), ((key&0xF)<<4)|((val&0xF00)>>8), (val&0xFF),  0 ]
    tx[3]=(tx[0]+tx[1]+tx[2])&0x7F

    ser.write(b'\x84')
    #time.sleep(0.003)
    waitCam()
    ser.write(tx)
    #time.sleep(0.01)
    waitCam()

connected=False
while(not connected):
    ser.write(b'\x80')
    r=ser.read()
    if(r == b'\x80'):
        ser.write(b'\xA0')
        connected=True
        print("connected")
    else:
        print("waiting")
    time.sleep(0.8)

sendCmd(0x7d, 0x1)

sendCmd("Colorbars", 0x0)

sendCmd(0x51, 0x1)	#ACK UNIPLM

sendCmd("White Bal", "A")

sendCmd("Autoiris", 0x0)

sendKey("Iris", 0x340)

sendCmd("Autoiris", 0x1)

sendKey("Autoiris", 0x340)

sendCmd("Autoiris", 0x1)

sendCmd("Auto White", 0x1,True)#request special transmission


sendCmd("White Bal", "Preset")

sendCmd("Shutter", "off")

sendCmd("Shutter", 0x1)	#ACK UNIPLM

sendCmd("Shutter", "1/120")

sendCmd("Shutter", "1/250")

sendCmd("Shutter", "1/500")

sendCmd("Shutter", "1/1000")

sendCmd("Shutter", "1/2000")

sendCmd("Shutter", 0xf)	#ACK UNIPLM

sendKey(0x56, 0x26e)	#ACK UNIPLM

sendCmd("Shutter", "off")

sendKey("Black", 0x310)

sendCmd("Auto White", 0x0,True)#request special transmission
	#ACK UNIPLM

sendCmd("White Bal", 0x0)

sendCmd("White Bal", "Preset")

sendCmd("White Bal", "A")

sendCmd("White Bal", "B")

sendCmd("White Bal", "full auto")

sendCmd("White Bal", "A")

sendKey("Red", 0x328)

sendKey("Blue", 0x230)

sendCmd("White Bal", "B")

sendKey("Red", 0x404)

sendKey("Blue", 0x41c)

sendCmd("White Bal", 0x0)

sendKey(0x02, 0x33c)

sendKey(0x03, 0x368)

sendCmd("White Bal", "Preset")

sendCmd("Gain", "0dB")

sendCmd("Gain", "6dB")

sendCmd("Gain", "9dB")

sendCmd("Gain", "12dB")

sendCmd("Gain", "18dB")

sendCmd("Gain", 0x5)	#ACK UNIPLM

sendCmd("Gain", 0x6)	#ACK UNIPLM

sendCmd("Gain", 0x8)

sendCmd("Gain", "3dB")

sendCmd("Gain", 0xe)	#ACK UNIPLM

sendKey(0x74, 0x801)	#ACK UNIPLM

sendCmd(0x51, 0x1)	#ACK UNIPLM

sendCmd(0x51, 0x0)	#ACK UNIPLM

sendCmd("Gain", "0dB")

sendCmd(0x08, 0x1)

sendCmd(0x53, 0x1)

sendCmd(0x08, 0x0)

sendCmd(0x53, 0x0)

sendCmd("Call", 0x1)

sendCmd("Call", 0x0)

sendCmd("black mod", "stretch")

sendCmd("black mod", "compress")

sendCmd("black mod", "unmod")

sendCmd(0x4b, 0x0)	#ACK UNIPLM

sendCmd(0x4b, 0x2)	#ACK UNIPLM

sendCmd(0x4b, 0xf)	#ACK UNIPLM

sendCmd(0x4b, 0x1)	#ACK UNIPLM

sendCmd(0x4c, 0x0)

sendCmd(0x4c, 0x2)

sendCmd(0x4c, 0xf)	#ACK UNIPLM

sendCmd(0x4c, 0x1)

sendCmd(0x4f, 0x1)	#ACK UNIPLM

sendCmd(0x4f, 0x2)	#ACK UNIPLM

sendCmd(0x4f, 0x0)	#ACK UNIPLM

sendCmd(0x1b, 0x1)	#ACK UNIPLM

sendCmd(0x1b, 0x0)	#ACK UNIPLM

sendKey(0x12, 0x530)	#ACK UNIPLM

sendCmd("Detail", 0x0)

sendKey(0x14, 0x400)

sendKey(0x16, 0x400)

sendCmd(0x4c, 0x1)

sendCmd("Skin Detail", 0x0)

sendCmd("Auto Knee", 0x0)

sendKey(0x32, 0x604)

sendCmd(0x4e, 0x1)	#ACK UNIPLM

sendCmd(0x1b, 0x0)	#ACK UNIPLM

sendCmd(0x1d, 0x0)

sendKey(0x36, 0x114)

sendCmd("black mod", "unmod")

sendCmd(0x4f, 0x0)	#ACK UNIPLM

sendCmd("DNR", 0x0)

sendCmd(0x4b, 0x1)	#ACK UNIPLM

sendCmd(0x52, 0x0)

sendKey(0xf3, 0xf7c)	#ACK UNIPLM

sendKey(0xf2, 0x8)	#ACK UNIPLM

sendKey(0xf2, 0xc)	#ACK UNIPLM

sendKey(0xf2, 0x80c)	#ACK UNIPLM

sendKey(0xf3, 0xc)	#ACK UNIPLM

sendCmd("Gain", "0dB")

sendCmd("Colorbars", 0x0)

sendCmd(0x50, 0x1)

SpecialTransmitt(0)

sendCmd("Call", 0x0)

sendCmd("Gain", "0dB")

sendCmd(0x53, 0x0)

sendCmd(0x08, 0x0)

sendCmd("Full Auto Shooting", 0x0)
while True:
    time.sleep(1)
    sendCmd(0x0,0x1)
    time.sleep(1)
    sendCmd(0x0,0x0)
    time.sleep(1)
    sendCmd("Gain", "0dB")
    time.sleep(1)
    sendCmd("Gain", "3dB")
    time.sleep(1)
    sendCmd("Gain", "6dB")
    time.sleep(1)
    sendCmd("Gain", "9dB")
    time.sleep(1)
    sendCmd("Gain", "12dB")
    time.sleep(1)
    sendCmd("Gain", "18dB")

