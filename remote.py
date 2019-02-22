#! /usr/bin/env python3
# send jvc ccu RM-P210 commands
import serial
import csv
import time
import numpy as np
np.set_printoptions(formatter={'int':hex})

verbose = False

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

def waitCam(verb=False):
    verb=verbose|verb

    rcv=False
    retry_count=0
    while(not rcv and retry_count < 2):
        r = ser.read()
        try:
            r=ord(r)
            if verb:
                print("cam: "+hex(r))
            rcv=True
        except TypeError:
            if(verbose):
                print("waiting for CAM...")
            rcv=False
            retry_count+=1
            continue

    if(not rcv):
        if(verb):
            print("CAM did not respond ...")
        return "no response"
    elif(r == 0xA0):
        if(verb):
            print("cam: ACK")
        return True
    elif(r >= 0xF0):
        if verb:
            print("application ERROR: "+hex(r))
        return r
    if(verbose):
        print("passing input to handle Cam: "+hex(r))
    return handleCam(r)

def handleCam(r):
    try:
        r=ord(r)
        if verbose:
            print("hadeling cam: "+hex(r))
    except TypeError:
        if type(r) is int:
            pass
        else:
            #if verbose:
            #    print("nothing to handle; going on ...")
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
            print("cam: ", end="")
            print(np.array(packet))

        if((packet[0] + packet[1]) & 0x7F != (packet[2])):
            print("checksum ERROR")
            print(np.array(packet))
            print("re-handling...")
            ser.flushInput()
            handleCam(ser.read())
        else:
            cmd = packet[1]
            data = (packet[0] & 0x0F)
            bitflags = (packet[0] & 0xF0) >> 4

            print("cam: ", end="")
            decode(cmd, data, cmd_id)

            if((bitflags & 0x2) and verbose):
                print("request special transmission")
        return "got message from cam"
    elif(r==0x80):
        if(verbose):
            print("CAM seems to be unconnected!")
            print("trying to reconnect")
        connect()
        SpecialTransmitt(0)
        return "connection lost; reconnected"
    else:
        print("Cam sent: "+str(r))
        print("unhandled special request response? "+hex(r)+"; sending ACK ...")
        ser.write(b'\xA0')
        handleCam(ser.read())

def sendCmd(cmd, data, special=False):
    handleCam(ser.read())

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
        tx[0]=tx[0]| 0x20
    tx[2]=(tx[0]+tx[1]) & 0x7F

    if verbose:
        print("sending: ",end="")
        decode(cmd,data,cmd_id)

    if(verbose):
        print("starting transmission")
    ser.write(b'\x83')
    ret=waitCam()
    if not ret:
        if(type(ret) is bool):
            print("Cam not ACKing our transmission")
        elif(type(ret) is int):
            print("Cam not ACKing our transmission; resp: "+hex(ret))
            handleCam(ret)
        #sendCmd(cmd, data, special)
    ser.write(tx)
    print("sending packet: "+str(np.array(tx)))

    ret=waitCam()
    if not ret:
        print("cam sent:"+hex(ret));
    return ret

def sendKey(key, val):
    handleCam(ser.read())
    if(type(key) is str):
        found = False
        for x in key_id:
            if(x[5]==key):
                found = True
                key=int(x[1],0)
        if( not found ):
            print("unknown string: \""+key+"\"")
            return -1

    if(type(val) is str):
        found = False
        for x in key_id:
            if(int(x[1],0)==key and x[6]==val):
                found = True
                val=int(x[2],0)
        if( not found ):
            print("unknown string: \""+val+"\"")
            return -1

    #key = (packet[0] << 4) | ((packet[1] & 0xF0) >> 4)
    #val = ((packet[1] & 0x0F) << 8) | packet[2]
    tx = [ ((key&0xFF0) >> 4), ((key&0xF)<<4)|((val&0x780)>>7), (val&0x7F),  0 ]
    tx[3]=(tx[0]+tx[1]+tx[2])&0x7F

    if verbose:
        print("sending: ",end="")
        decode(key,val,key_id)

    ser.write(b'\x84')
    ret=waitCam()
    if not ret:
        if verbose:
            print("aborting")
        return ret
    ser.write(tx)
    if(verbose):
        print("wrote: ", end="")
        print(np.array(tx))
    ret=waitCam()

   # if not ret:
   #     if(type(ret) is bool):
   #         print("Cam not ACKing our transmission")
   #     elif(type(ret) is int):
   #         print("Cam not ACKing our transmission; resp: "+hex(ret))
   #         handleCam(ret)


    if not ret:
        if(verbose):
            if(type(ret) is str):
                print("Cam not ACKing our transmission")
            elif(type(ret) is int):
                print("Cam sent ERROR: "+hex(ret))
            else:
                print("")
        #sendKey(key, val)
    return ret

def SpecialTransmitt(data):
    if(verbose):
            print("#### Special Transmit beginn ####")

    handleCam(ser.read())
    tx=0x90|data
    print("write: "+hex(tx))
    ser.write(bytearray([tx]))
    ret=waitCam(True)
    if not ret:
        return ret

    waitCam(True)

    if(verbose):
        print("#### Special Transmit end ####")
    return "OK"

def init_cam():
    ser.flushInput()
    connect()

    sendCmd(0x7d, 0x1)
#    sendCmd("Colorbars", 0x0)
#    sendCmd(0x51, 0x1)	#ACK; UNIPLM
#    sendCmd("White Bal", "A")
#    sendCmd("Autoiris", 0x0)
#    sendKey("Iris", 0x0)
#    sendCmd("Autoiris", 0x1)
#    sendKey("Autoiris", 0x0)
#    sendCmd("Autoiris", 0x1)
#    sendCmd("Auto White", 0x1,True)#request special transmission
#    sendCmd("White Bal", "Preset")
#    sendCmd("Shutter", "off")
#    sendCmd("Shutter", 0x1)	#ACK; UNIPLM
#    sendCmd("Shutter", "1/120")
#    sendCmd("Shutter", "1/250")
#    sendCmd("Shutter", "1/500")
#    sendCmd("Shutter", "1/1000")
#    sendCmd("Shutter", "1/2000")
#    sendCmd("Shutter", 0xf)	#ACK; UNIPLM
#    sendKey(0x56, 0x26e)	#ACK; UNIPLM
#    sendCmd("Shutter", "off")
#    sendKey("Black", 0x540)
#    sendCmd("Auto White", 0x0,True)#request special transmission
#    	#ACK; UNIPLM
#    sendCmd("White Bal", 0x0)
#    sendCmd("White Bal", "Preset")
#    sendCmd("White Bal", "A")
#    sendCmd("White Bal", "B")
#    sendCmd("White Bal", "full auto")
#    sendCmd("White Bal", "A")
#    sendKey("Red", 0x51c)
#    sendKey("Blue", 0x254)
#    sendCmd("White Bal", "B")
#    sendKey("Red", 0x404)
#    sendKey("Blue", 0x41c)
#    sendCmd("White Bal", 0x0)
#    sendKey(0x02, 0x33c)
#    sendKey(0x03, 0x368)
#    sendCmd("White Bal", "A")
#    sendKey("Red", 0x400)
#    sendKey("Blue", 0x400)
#    sendCmd("Gain", "0dB")
#    sendCmd("Gain", "6dB")
#    sendCmd("Gain", "9dB")
#    sendCmd("Gain", "12dB")
#    sendCmd("Gain", "18dB")
#    sendCmd("Gain", 0x5)	#ACK; UNIPLM
#    sendCmd("Gain", 0x6)	#ACK; UNIPLM
#    sendCmd("Gain", "ALC")
#    sendCmd("Gain", "3dB")
#    sendCmd("Gain", 0xe)	#ACK; UNIPLM
#    sendKey(0x74, 0x801)	#ACK; UNIPLM
#    sendCmd(0x51, 0x1)	#ACK; UNIPLM
#    sendCmd(0x51, 0x0)	#ACK; UNIPLM
#    sendCmd("Gain", "0dB")
#    sendCmd("Tally PGM", 0x1)
#    sendCmd("Tally PVW", 0x1)
#    sendCmd("Tally PGM", 0x0)
#    sendCmd("Tally PVW", 0x0)
#    sendCmd("Call", 0x1)
#    sendCmd("Call", 0x0)
#    sendCmd("black mod", "stretch")
#    sendCmd("black mod", "compress")
#    sendCmd("black mod", "unmod")
#    sendCmd(0x4b, 0x0)	#ACK; UNIPLM
#    sendCmd(0x4b, 0x2)	#ACK; UNIPLM
#    sendCmd(0x4b, 0xf)	#ACK; UNIPLM
#    sendCmd(0x4b, 0x1)	#ACK; UNIPLM
#    sendCmd(0x4c, 0x0)
#    sendCmd(0x4c, 0x2)
#    sendCmd(0x4c, 0xf)	#ACK; UNIPLM
#    sendCmd(0x4c, 0x1)
#    sendCmd(0x4f, 0x1)	#ACK; UNIPLM
#    sendCmd(0x4f, 0x2)	#ACK; UNIPLM
#    sendCmd(0x4f, 0x0)	#ACK; UNIPLM
#    sendCmd(0x1b, 0x1)	#ACK; UNIPLM
#    sendCmd(0x1b, 0x0)	#ACK; UNIPLM
#    sendKey(0x12, 0x530)	#ACK; UNIPLM
#    sendCmd("Detail", 0x0)
#    sendKey(0x14, 0x400)
#    sendKey(0x16, 0x400)
#    sendCmd(0x4c, 0x1)
#    sendCmd("Skin Detail", 0x0)
#    sendCmd("Auto Knee", 0x0)
#    sendKey(0x32, 0x604)
#    sendCmd(0x4e, 0x1)	#ACK; UNIPLM
#    sendCmd(0x1b, 0x0)	#ACK; UNIPLM
#    sendCmd("Add Brightness", 0x0)
#    sendKey(0x36, 0x114)
#    sendCmd("black mod", "unmod")
#    sendCmd(0x4f, 0x0)	#ACK; UNIPLM
#    sendCmd("DNR", 0x0)	#ACK; UNIPLM
#    sendCmd(0x4b, 0x1)	#ACK; UNIPLM
#    sendCmd(0x52, 0x0)
#    sendKey(0xf3, 0xf7c)	#ACK; UNIPLM
#    sendKey(0xf2, 0x8)	#ACK; UNIPLM
#    sendKey(0xf2, 0xc)	#ACK; UNIPLM
#    sendKey(0xf2, 0x80c)	#ACK; UNIPLM
#    sendKey(0xf3, 0xc)	#ACK; UNIPLM
#    sendCmd("Gain", "0dB")
#    sendCmd("Colorbars", 0x0)
#    sendCmd("Full Auto Shooting", 0x0)
#            #unknown packet: 0x90
#    SpecialTransmitt(0)
#    sendCmd("Call", 0x0)
#    sendCmd("Gain", "0dB")
#    sendCmd("Shutter", "off")
#    sendCmd("Tally PVW", 0x0)
#    sendCmd("Tally PGM", 0x0)
#    sendCmd(0x0b, 0x0)
    SpecialTransmitt(0)

def autowhite():
    tmp=ser.timeout
    sendCmd("Auto White", 0x1)
    ser.timeout=3
    ans=ord(ser.read())
    ser.write(b'\xA0')
    ser.timeout=tmp

    if(ans==0x90):
        print("Auto White OK")
        waitCam(True)
        waitCam(True)
    elif(ans==0x92):
        print("Auto White failed, maybe Low Light or in Preset mode")
    elif(ans==0x94):
        print("Auto White failed: Over Light")
    elif(ans==0x96):
        print("Auto White failed: Improper Object")
    else:
        print("Unknown Answer...")
        print(hex(ans))


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


