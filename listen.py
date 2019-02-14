#! /usr/bin/env python3
# decode jvc ccu RM-P210 commands
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, parity=serial.PARITY_EVEN)

gainTable = {
     64  : 0,
     66  : 9,
     68  : 18
#    0  : 0,
#    10 : 3,
#    1  : 6,
#    2  : 9,
#    3  : 13,
#    4  : 18
    }

while True:
    length = ord(ser.read())
    print(hex(length))

    if (length & 0x80):
        length = length & 0x0F
        buff = ser.read(length)
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
            elif key == 64 and val == 487547:
                print("Autoiris")

            #checksum
            print(((packet[0] + packet[1] + packet[2]) & 0x7F) == packet[3])
        elif length == 3:
            cmd = packet[1]
            data = (packet[0] & 0x7F)
            if (cmd == 6):
                print("Auto White")
                ser.read()
                print("Done!")
            elif (cmd == 7):
                print("Gain: %02idB" % gainTable[data])
            elif (cmd == 2):
                if(data == 65):
                    print("autoiris: on")
                if(data == 64):
                    print("autoiris: off")
            else:
                print(bin(packet[0]))

            #checksum
            print((cmd + data) == packet[2])
        print("")


