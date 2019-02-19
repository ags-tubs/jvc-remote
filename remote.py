#! /usr/bin/env python3
# send jvc ccu RM-P210 commands
import serial
import csv
import time
import numpy as np
np.set_printoptions(formatter={'int':hex})

verbose = True

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

def connect():
    connected=False
    ser.flushInput()
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
    sendCmd(0,0)

def waitCam(verbose=False):
    rcv=False
    retry_count=0
    while(not rcv and retry_count < 2):
        r = ser.read()
        try:
            r=ord(r)
            #if verbose:
            #    print("cam: "+hex(r))
            rcv=True
        except TypeError:
            if(retry_count < 1):
                print("waiting for CAM...")
            rcv=False
            retry_count+=1
            continue

    if(not rcv):
        if(verbose):
            print("CAM did not respond ...")
        return False
    if(r == 0xA0):
        if(verbose):
            print("cam: ACK")
        return True
    elif((r & 0xF0) == 0xF0):
        print("application ERROR: "+hex(r))
        return False
    handleCam(r)

def handleCam(r):
    try:
        r=ord(r)
        if verbose:
            print("hadeling cam: "+hex(r))
    except TypeError:
        if type(r) is int:
            pass
        else:
            if verbose:
                print("nothing to handle; going on ...")
            return

    if(r == 0x83):
        print("CAM transmitting")
        packet = []
        ser.write(b'\xA0')
        buff = ser.read(3)
        ser.write(b'\xA0')
        for x in buff:
            packet.append(x)
        if verbose:
            print(np.array(packet))

        if((packet[0] + packet[1]) & 0x7F != (packet[2])):
            print("checksum ERROR")
            print(np.array(packet))
            ser.flushInput()
        else:
            cmd = packet[1]
            data = (packet[0] & 0x0F)
            bitflags = (packet[0] & 0xF0) >> 4

            decode(cmd, data, cmd_id)

            if(bitflags & 0x2):
                print("request special transmission")
    elif(r==0x80):
        print("CAM seems to be unconnected!")
        print("trying to reconnect")
        connect()
        SpecialTransmitt(0)
    else:
        print("Cam sent: "+hex(r))
        print("unhandled special request response? "+hex(r)+"; sending ACK ...")
        ser.write(b'\xA0')
        handleCam(ser.read())


def SpecialTransmitt(data):
    print("#### Special Transmit beginn ####")

    handleCam(ser.read())
    tx=0x90|data
    print("write: "+hex(tx))
    ser.write(bytearray([tx]))
    waitCam(True)
    waitCam(True)

    print("#### Special Transmit end ####")

def sendCmd(cmd, data, special=False):
    handleCam(ser.read())
    print("sendCmd "+str(cmd)+" = "+str(data), end='')

    if(type(cmd) is str):
        found = False
        for x in cmd_id:
            if(x[5]==cmd):
                found = True
                cmd=int(x[1],0)
        if( not found ):
            print("unknown string: \""+cmd+"\"")
            return

    if(type(data) is str):
        found = False
        for x in cmd_id:
            if(int(x[1],0)==cmd and x[6]==data):
                found = True
                data=int(x[2],0)
        if( not found ):
            print("unknown string: \""+data+"\"")
            return

    tx=[data|0x40,cmd,0]
    if(special):
        tx[0]=tx[0]|0x2
    tx[2]=(tx[0]+tx[1])&0x7F

    ser.write(b'\x83')
    if(not waitCam()):
        sendCmd(cmd, data, special)
    ser.write(tx)
    print(np.array(tx),end='\t')
    if(waitCam(True)):
        print(hex(data));

def sendKey(key, val):
    handleCam(ser.read())
    print("sendKey "+str(key)+" = "+str(val), end='\t')
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
    if(not waitCam()):
        print("aborting")
        return
    ser.write(tx)
    print(np.array(tx),end='\t')
    if(not waitCam(True)):
        print("aborting")
        return
        #sendKey(key, val)

def init_cam():
    ser.flushInput()
    connect()
    SpecialTransmitt(0)

def autowhite():
    tmp=ser.timeout
    ser.timeout=3
    sendCmd("Auto White", 0x1)
    ans=ord(ser.read())
    ser.write(b'\xA0')
    ser.timeout=tmp

    if(ans==0x90):
        print("Auto White OK")
    elif(ans==0x92):
        print("Auto White failed, maybe Low Light or in Preset mode")
    elif(ans==0x94):
        print("Auto White failed: Over Light")
    elif(ans==0x96):
        print("Auto White failed: Improper Object")
    else:
        print("Unknown Answer...")
        print(hex(ans))

    sendCmd("Full Auto Shooting", 0x0)

def fun():
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

def decode(feature_id, value, table):
    found = False
    for x in table:
        if((int(x[1],0)==feature_id) and (int(x[2],0)==value) and (x[6] != "") and not found):
            found=True
            if(x[5]==""):
                #topic="ID \'"+x[1]+"\'"
                topic=x[1]
            else:
                topic="\""+x[5]+"\""

            #print("send"+x[0]+"("+topic+", \""+x[6]+"\")\t")
            print("set "+topic+" to "+x[6])
            break
    if(not found):
        for x in table:
            if(int(x[1],0)==feature_id and not found):
                found=True
                if(x[5]==""):
                    #topic="ID \'"+x[1]+"\'"
                    topic=x[1]
                else:
                    topic="\""+x[5]+"\""

                #print("send"+x[0]+"("+topic+", "+hex(value)+")", end='')
                print("set "+topic+" to \'"+hex(value)+"\'")
                break
    if(not found):
        print("set ID '"+hex(feature_id)+"' to \'"+hex(value)+"\'")
        #print("send"+x[0]+"("+hex(feature_id)+", "+hex(value)+")", end='')
    #print("send"+x[0]+"("+hex(feature_id)+","+hex(value)+")")

def getGainValues():
    for x in range(0, 0xf):
        sendCmd("Gain",x)

