#! /usr/bin/env python3
# decode jvc ccu RM-P210 commands
import serial

#method="serial"
method="stdin"

if(method=="serial"):
    ser = serial.Serial('/dev/ttyUSB0', 9600, parity=serial.PARITY_EVEN)

#ser_cam = serial.Serial('/dev/ttyUSB1', 9600, parity=serial.PARITY_EVEN)

gainTable = {
     64  : "0dB",
     65  : "6dB",
     66  : "9dB",
     67  : "12dB",
     68  : "18dB",
     72  : "auto(?)",
     74  : "3dB",
#    0  : 0,
#    10 : 3,
#    1  : 6,
#    2  : 9,
#    3  : 13,
#    4  : 18
    }


shutterTable = {
    64 : "off",
    66 : "1/120",
    67 : "1/250",
    68 : "1/500",
    69 : "1/1000",
    70 : "1/2000",
}

#def readCam():
#    ser_cam.timeout=0.0035
#    camNotEmpty=True
#    while(camNotEmpty):
#        cam = ser_cam.read()
#        try:
#            print("cam: "+cam)
#        except TypeError:
#            camNotEmpty=False

def readBytes(length):
    buff = []
    if(method=="stdin"):
        try:
            for x in range(0, int(length)):
                buff.append(int("0x"+input(),0))
        except EOFError:
            print("reached file end; exiting");
            exit()
    if(method=="serial"):
        bts = ser.read(length)
        for v in bts:
            buff += [ord(v)]

    return buff

#readBytes(2)

while True:
    length = readBytes(1)[0]
    print("ccu: "+hex(length))
#    readCam()

    if (int(length) & 0x80):

        length = length & 0x0F
        buff = readBytes(length)
        packet = []
        for v in buff:
            packet += [v]
        print(packet)
        if length == 4:
            key = (packet[0] << 4) | ((packet[1] & 0xF0) >> 4)
            val = ((packet[1] & 0x0F) << 8) | packet[2]
            if key == 0:
                print("Iris: %i" % val)
            elif key == 6:
                print("Black %i" % val)
            elif key == 38:
                print("Red %i" % val)
            elif key == 39:
                print("Blue %i" % val)
            elif key == 64:
                print("Autoiris manipulation: %i" % val)
            else:
                print("Unkown key: "+hex(key))

            #checksum
            print(((packet[0] + packet[1] + packet[2]) & 0x7F) == packet[3])
        elif length == 3:
            cmd = packet[1]
            data = (packet[0] & 0x7F)

            if (cmd == 0):
                if(data == 65):
                    print("colorbars: on")
                elif(data == 64):
                    print("colorbars: off")
                else:
                    print("colorbars UNKNOWN?!?!")

            elif (cmd == 1):
                if(data == 65):
                    print("Detail: on")
                elif(data == 64):
                    print("Detail: off")
                else:
                    print("Detail UNKNOWN?!?!")

            elif (cmd == 2):
                if(data == 65):
                    print("autoiris: on")
                elif(data == 64):
                    print("autoiris: off")
                else:
                    print("autoiris UNKNOWN?!?!")

            elif (cmd == 3):
                if(data == 65):
                    print("White Bal: Preset")
                elif(data == 66):
                    print("White Bal: A")
                elif(data == 67):
                    print("White Bal: B")
                elif(data == 79):
                    print("Full Auto White: on")
                else:
                    print("White Bal UNKNOWN?!?!")

            elif (cmd == 6):
                print("Auto White")
                #ser.read()
                #print("Done!")

            elif (cmd == 7):
                try:
                    print("Gain: "+gainTable[data])
                except KeyError:
                    print("Unknown Gain Value ?!?!")

            elif (cmd == 9):
                if(data == 64):
                    print("Call: off")
                elif(data == 65):
                    print("Call: on")
                else:
                    print("intercom UNKNOWN?!?!")

            elif (cmd == 12):
                try:
                    print("Shutter: " + shutterTable[data])
                except KeyError:
                    print("Shutter UNKNOWN?!?!")

            elif (cmd == 15):
                if(data == 66):
                    print("black compress: on")
                elif(data == 65):
                    print("black stretch: on")
                elif(data == 64):
                    print("black unmodified")
                else:
                    print("black compress UNKNOWN?!?!")

            elif (cmd == 28):
                if(data == 64):
                    print("Auto Knee: off")
                elif(data == 65):
                    print("Auto Knee: on")
                else:
                    print("Auto Knee UNKNOWN?!?!")

            elif (cmd == 74):
                if(data == 64):
                    print("DNR: off")
                elif(data == 65):
                    print("DNR: on")
                else:
                    print("DNR UNKNOWN?!?!")

            elif (cmd == 77):
                if(data == 64):
                    print("Skin Detail: off")
                elif(data == 65):
                    print("Skin Detail: on")
                else:
                    print("Skin Detail UNKNOWN?!?!")

            else:
                print(hex(packet[0]) + " Unknown Command ?!?!")

            #checksum
            print((cmd + data) == (packet[2] & 0x7F))
#        readCam()
        print("")


