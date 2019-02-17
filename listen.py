#! /usr/bin/env python3
# decode jvc ccu RM-P210 commands
import serial
import numpy as np
np.set_printoptions(formatter={'int':hex})

#method="serial"
method="stdin"

if(method=="serial"):
    ser = serial.Serial('/dev/ttyUSB0', 9600, parity=serial.PARITY_EVEN)

#ser_cam = serial.Serial('/dev/ttyUSB1', 9600, parity=serial.PARITY_EVEN)

def decodeCam(cam_byte, verbose=False):
    if(cam_byte == "cam: F2"):
        print(",UNIPLM")
    elif(cam_byte == "cam: A0"):
        if(verbose):
            print(",IMPL")
    else:
        print(cam_byte)

def readBytes(length):
    buff = []

    if(method=="stdin"):
        for x in range(0, int(length)):
            inp=input()
            try:
                buff.append(int("0x"+inp,0))
            except EOFError:
                print("reached file end; exiting");
                exit()
            except ValueError:
                decodeCam(inp)
                return readBytes(length)


    if(method=="serial"):
        bts = ser.read(length)
        for v in bts:
            buff += [ord(v)]

    return buff

while True:
    length = readBytes(1)[0]

    if (int(length) & 0x80):
        length = length & 0x0F

        packet = readBytes(length)

        if length == 4:
            key = (packet[0] << 4) | ((packet[1] & 0xF0) >> 4)
            val = ((packet[1] & 0x0F) << 8) | packet[2]
            #"cmd type","key","value","bitfield","cam response","topic"
            print("key,"+"0x{:02x}".format(key)+","+"0x{:03x}".format(val)+",", end='')

            #checksum
            if(((packet[0] + packet[1] + packet[2]) & 0x7F) != packet[3]):
                print("checksum ERROR")
        elif length == 3:
            cmd = packet[1];
            bitfield = (packet[0] & 0xF0) >> 4
            data = (packet[0] & 0x0F)
            #"cmd type","key","value","bitfield","cam response","topic"
            print("cmd,"+"0x{:02x}".format(cmd)+","+"0x{:02x}".format(data)+","+"0b{:04b}".format(bitfield), end = '')

            #checksum
            if((packet[0] + packet[1]) & 0x7F != (packet[2])):
                print("checksum ERROR")

        decodeCam(input(), True)
