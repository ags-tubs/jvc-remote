#! /usr/bin/env python3
# decode jvc ccu RM-P210 commands
import serial
import csv
import numpy as np
np.set_printoptions(formatter={'int':hex})

#method="serial"
method="stdin"

if(method=="serial"):
    ser = serial.Serial('/dev/ttyUSB0', 9600, parity=serial.PARITY_EVEN)

#ser_cam = serial.Serial('/dev/ttyUSB1', 9600, parity=serial.PARITY_EVEN)

key_id = []
cmd_id = []

with open('cmds.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if(row[0]=="key"):
            key_id.append(row)
        if(row[0]=="cmd"):
            cmd_id.append(row)


#def readCam():
#    ser_cam.timeout=0.0035
#    camNotEmpty=True
#    while(camNotEmpty):
#        cam = ser_cam.read()
#        try:
#            print("cam: "+cam)
#        except TypeError:
#            camNotEmpty=False
def decodeCam(cam_byte, verbose=False):
    if(cam_byte == "cam: F2"):
        print("\tACK; UNIPLM")
    elif(cam_byte == "cam: A0"):
        if(verbose):
            print("\tACK")
        else:
            print()
    else:
        print(cam_byte)

def readBytes(length):
    buff = []

    if(method=="stdin"):
        for x in range(0, int(length)):
            try:
                inp=input()
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
    #print("ccu: "+hex(length))
#    readCam()

    if (int(length) & 0x80):
        length = length & 0x0F

        packet = readBytes(length)
        #print(np.array(packet))

        if length == 4:
            if(((packet[0] + packet[1] + packet[2]) & 0x7F) != packet[3]):
                print("checksum ERROR")
            else:
                key = (packet[0] << 4) | ((packet[1] & 0xF0) >> 4)
                val = ((packet[1] & 0x0F) << 8) | packet[2]

                found = False

                for x in key_id:
                    if((int(x[1],0)==key) and (int(x[1],0)==val) and not found):
                        found=True
                        if(x[5]==""):
                            topic="ID \'"+x[1]+"\'"
                        else:
                            topic=x[5]

                        if(x[6]==""):
                            setting="\'"+x[2]+"\'"
                        else:
                            setting=x[6]

                        print("set "+topic+" to "+setting+"\t", end='')
                        break

                if(not found):
                    for x in key_id:
                        if(int(x[1],0)==key and not found):
                            found=True
                            if(x[5]==""):
                                topic="ID \'"+x[1]+"\'"
                            else:
                                topic=x[5]

                            print("set "+topic+" to \'"+x[2]+"\'", end='')
                            break

                if(not found):
                    print("set ID '"+x[1]+"' to \'"+x[2]+"\'\t", end='\t')

        elif length == 3:
            if((packet[0] + packet[1]) & 0x7F != (packet[2])):
                print("checksum ERROR")
            else:
                cmd = packet[1]
                data = (packet[0] & 0x0F)

                found = False

                for x in cmd_id:
                    if((int(x[1],0)==cmd) and (int(x[1],0)==data) and not found):
                        found=True
                        if(x[5]==""):
                            topic="ID \'"+x[1]+"\'"
                        else:
                            topic=x[5]

                        if(x[6]==""):
                            setting="\'"+x[2]+"\'"
                        else:
                            setting=x[6]

                        print("set "+topic+" to "+setting+"\t", end='')
                        break

                if(not found):
                    for x in cmd_id:
                        if(int(x[1],0)==cmd and not found):
                            found=True
                            if(x[5]==""):
                                topic="ID \'"+x[1]+"\'"
                            else:
                                topic=x[5]

                            print("set "+topic+" to \'"+x[2]+"\'"+"\t", end='')
                            break

                if(not found):
                    print("set ID '"+x[1]+"' to \'"+x[2]+"\'"+"\t", end='')

    decodeCam(input())
