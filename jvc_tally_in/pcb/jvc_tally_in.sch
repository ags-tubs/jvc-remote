EESchema Schematic File Version 5
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
Comment5 ""
Comment6 ""
Comment7 ""
Comment8 ""
Comment9 ""
$EndDescr
Connection ~ 3100 3700
Connection ~ 3450 1550
Connection ~ 3900 2050
Connection ~ 4400 1550
Connection ~ 5300 3150
Connection ~ 6150 3750
Connection ~ 6250 3850
Connection ~ 7700 3850
NoConn ~ 2950 3600
NoConn ~ 7400 1750
Wire Wire Line
	1700 3650 1800 3650
Wire Wire Line
	1850 1650 1700 1650
Wire Wire Line
	1850 1750 1700 1750
Wire Wire Line
	2000 1400 2000 1550
Wire Wire Line
	2000 1550 1700 1550
Wire Wire Line
	2000 1850 1700 1850
Wire Wire Line
	2000 2000 2000 1850
Wire Wire Line
	2100 3650 2150 3650
Wire Wire Line
	2150 3600 2350 3600
Wire Wire Line
	2150 3650 2150 3600
Wire Wire Line
	2150 3750 1700 3750
Wire Wire Line
	2150 3800 2150 3750
Wire Wire Line
	2350 3800 2150 3800
Wire Wire Line
	3100 3100 3100 3250
Wire Wire Line
	3100 3550 3100 3700
Wire Wire Line
	3100 3700 2950 3700
Wire Wire Line
	3100 3800 2950 3800
Wire Wire Line
	3100 3950 3100 3800
Wire Wire Line
	3300 3700 3100 3700
Wire Wire Line
	3450 1400 3450 1550
Wire Wire Line
	3450 1550 3600 1550
Wire Wire Line
	3450 1750 3450 1550
Wire Wire Line
	3450 1950 3450 2050
Wire Wire Line
	3450 2050 3900 2050
Wire Wire Line
	3900 2050 3900 1850
Wire Wire Line
	3900 2150 3900 2050
Wire Wire Line
	4400 1400 4400 1550
Wire Wire Line
	4400 1550 4200 1550
Wire Wire Line
	4400 1750 4400 1550
Wire Wire Line
	4400 1950 4400 2050
Wire Wire Line
	4400 2050 3900 2050
Wire Wire Line
	4650 3150 4900 3150
Wire Wire Line
	4650 3250 4650 3150
Wire Wire Line
	5100 3150 5300 3150
Wire Wire Line
	5300 3150 5300 3000
Wire Wire Line
	5300 3150 5300 3450
Wire Wire Line
	5300 4750 5300 4650
Wire Wire Line
	5900 4050 6450 4050
Wire Wire Line
	6150 3450 6150 3750
Wire Wire Line
	6150 3750 5900 3750
Wire Wire Line
	6250 3450 6250 3850
Wire Wire Line
	6250 3850 5900 3850
Wire Wire Line
	6250 3850 7300 3850
Wire Wire Line
	6450 3750 6150 3750
Wire Wire Line
	6450 3950 5900 3950
Wire Wire Line
	6800 1650 6900 1650
Wire Wire Line
	6800 1750 6900 1750
Wire Wire Line
	6900 1850 6800 1850
Wire Wire Line
	7600 1550 7600 1650
Wire Wire Line
	7600 1650 7400 1650
Wire Wire Line
	7600 1850 7400 1850
Wire Wire Line
	7600 1950 7600 1850
Wire Wire Line
	7600 3850 7700 3850
Wire Wire Line
	7700 3400 7700 3500
Wire Wire Line
	7700 3800 7700 3850
Wire Wire Line
	7700 3850 7700 3950
Wire Wire Line
	7900 3400 7700 3400
Wire Notes Line
	1200 1050 2350 1050
Wire Notes Line
	1200 2350 1200 1050
Wire Notes Line
	1200 2800 1200 4300
Wire Notes Line
	1200 4300 3800 4300
Wire Notes Line
	2350 1050 2350 2350
Wire Notes Line
	2350 2350 1200 2350
Wire Notes Line
	3800 2800 1200 2800
Wire Notes Line
	3800 4300 3800 2800
Wire Notes Line
	5950 950  8300 950 
Wire Notes Line
	5950 2400 5950 950 
Wire Notes Line
	8300 950  8300 2400
Wire Notes Line
	8300 2400 5950 2400
Text Notes 1200 1000 0    50   ~ 0
Camera connector
Text Notes 1250 2750 0    50   ~ 0
Tally In
Text Notes 1500 3350 0    50   ~ 0
5V Input\n60mA LED current
Text Notes 6000 1150 0    50   ~ 0
TPI Programming Port\nevtentually 5V needed on 3V3 rail while programming !!!
Text GLabel 1850 1650 2    50   Input ~ 0
RX
Text GLabel 1850 1750 2    50   Input ~ 0
TX
Text GLabel 3300 3700 2    50   Input ~ 0
~TALLY
Text GLabel 6150 3450 1    50   Input ~ 0
TPIDATA
Text GLabel 6250 3450 1    50   Input ~ 0
TPICLK
Text GLabel 6450 3750 2    50   Input ~ 0
~TALLY
Text GLabel 6450 3950 2    50   Input ~ 0
TX
Text GLabel 6450 4050 2    50   Input ~ 0
RESET
Text GLabel 6800 1650 0    50   Input ~ 0
TPIDATA
Text GLabel 6800 1750 0    50   Input ~ 0
TPICLK
Text GLabel 6800 1850 0    50   Input ~ 0
RESET
Text GLabel 7900 3400 2    50   Input ~ 0
RX
$Comp
L power:+9V #PWR01
U 1 1 5E46CEAF
P 2000 1400
F 0 "#PWR01" H 2000 1250 50  0001 C CNN
F 1 "+9V" H 2015 1573 50  0000 C CNN
F 2 "" H 2000 1400 50  0001 C CNN
F 3 "" H 2000 1400 50  0001 C CNN
	1    2000 1400
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR03
U 1 1 5E4AE7C9
P 3100 3100
F 0 "#PWR03" H 3100 2950 50  0001 C CNN
F 1 "+3V3" H 3115 3273 50  0000 C CNN
F 2 "" H 3100 3100 50  0001 C CNN
F 3 "" H 3100 3100 50  0001 C CNN
	1    3100 3100
	-1   0    0    -1  
$EndComp
$Comp
L power:+9V #PWR05
U 1 1 5E46E6EB
P 3450 1400
F 0 "#PWR05" H 3450 1250 50  0001 C CNN
F 1 "+9V" H 3465 1573 50  0000 C CNN
F 2 "" H 3450 1400 50  0001 C CNN
F 3 "" H 3450 1400 50  0001 C CNN
	1    3450 1400
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR07
U 1 1 5E470674
P 4400 1400
F 0 "#PWR07" H 4400 1250 50  0001 C CNN
F 1 "+3V3" H 4415 1573 50  0000 C CNN
F 2 "" H 4400 1400 50  0001 C CNN
F 3 "" H 4400 1400 50  0001 C CNN
	1    4400 1400
	1    0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR09
U 1 1 5E47DA69
P 5300 3000
F 0 "#PWR09" H 5300 2850 50  0001 C CNN
F 1 "+3V3" H 5315 3173 50  0000 C CNN
F 2 "" H 5300 3000 50  0001 C CNN
F 3 "" H 5300 3000 50  0001 C CNN
	1    5300 3000
	-1   0    0    -1  
$EndComp
$Comp
L power:+3V3 #PWR011
U 1 1 5E485252
P 7600 1550
F 0 "#PWR011" H 7600 1400 50  0001 C CNN
F 1 "+3V3" H 7615 1723 50  0000 C CNN
F 2 "" H 7600 1550 50  0001 C CNN
F 3 "" H 7600 1550 50  0001 C CNN
	1    7600 1550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR02
U 1 1 5E46D5AF
P 2000 2000
F 0 "#PWR02" H 2000 1750 50  0001 C CNN
F 1 "GND" H 2005 1827 50  0000 C CNN
F 2 "" H 2000 2000 50  0001 C CNN
F 3 "" H 2000 2000 50  0001 C CNN
	1    2000 2000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR04
U 1 1 5E4AB936
P 3100 3950
F 0 "#PWR04" H 3100 3700 50  0001 C CNN
F 1 "GND" H 3105 3777 50  0000 C CNN
F 2 "" H 3100 3950 50  0001 C CNN
F 3 "" H 3100 3950 50  0001 C CNN
	1    3100 3950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR06
U 1 1 5E46F15D
P 3900 2150
F 0 "#PWR06" H 3900 1900 50  0001 C CNN
F 1 "GND" H 3905 1977 50  0000 C CNN
F 2 "" H 3900 2150 50  0001 C CNN
F 3 "" H 3900 2150 50  0001 C CNN
	1    3900 2150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR08
U 1 1 5E47EC21
P 4650 3250
F 0 "#PWR08" H 4650 3000 50  0001 C CNN
F 1 "GND" H 4655 3077 50  0000 C CNN
F 2 "" H 4650 3250 50  0001 C CNN
F 3 "" H 4650 3250 50  0001 C CNN
	1    4650 3250
	-1   0    0    -1  
$EndComp
$Comp
L power:GND #PWR010
U 1 1 5E47F9A0
P 5300 4750
F 0 "#PWR010" H 5300 4500 50  0001 C CNN
F 1 "GND" H 5305 4577 50  0000 C CNN
F 2 "" H 5300 4750 50  0001 C CNN
F 3 "" H 5300 4750 50  0001 C CNN
	1    5300 4750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR012
U 1 1 5E486351
P 7600 1950
F 0 "#PWR012" H 7600 1700 50  0001 C CNN
F 1 "GND" H 7605 1777 50  0000 C CNN
F 2 "" H 7600 1950 50  0001 C CNN
F 3 "" H 7600 1950 50  0001 C CNN
	1    7600 1950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR013
U 1 1 5E4D5323
P 7700 4250
F 0 "#PWR013" H 7700 4000 50  0001 C CNN
F 1 "GND" H 7705 4077 50  0000 C CNN
F 2 "" H 7700 4250 50  0001 C CNN
F 3 "" H 7700 4250 50  0001 C CNN
	1    7700 4250
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5E4A9F99
P 1950 3650
F 0 "R1" V 1743 3650 50  0000 C CNN
F 1 "60R" V 1834 3650 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 1880 3650 50  0001 C CNN
F 3 "~" H 1950 3650 50  0001 C CNN
	1    1950 3650
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 5E4AC388
P 3100 3400
F 0 "R2" V 2893 3400 50  0000 C CNN
F 1 "10k" V 2984 3400 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 3030 3400 50  0001 C CNN
F 3 "~" H 3100 3400 50  0001 C CNN
	1    3100 3400
	-1   0    0    1   
$EndComp
$Comp
L Device:R R3
U 1 1 5E4D2E55
P 7450 3850
F 0 "R3" V 7243 3850 50  0000 C CNN
F 1 "10k" V 7334 3850 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7380 3850 50  0001 C CNN
F 3 "~" H 7450 3850 50  0001 C CNN
	1    7450 3850
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 5E4E3DFC
P 7700 3650
F 0 "R4" H 7770 3696 50  0000 L CNN
F 1 "10k" H 7770 3605 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7630 3650 50  0001 C CNN
F 3 "~" H 7700 3650 50  0001 C CNN
	1    7700 3650
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C1
U 1 1 5E4662B7
P 3450 1850
F 0 "C1" H 3542 1895 50  0000 L CNN
F 1 "10u" H 3542 1805 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 3450 1850 50  0001 C CNN
F 3 "~" H 3450 1850 50  0001 C CNN
	1    3450 1850
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C2
U 1 1 5E466A85
P 4400 1850
F 0 "C2" H 4492 1895 50  0000 L CNN
F 1 "10u" H 4492 1805 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 4400 1850 50  0001 C CNN
F 3 "~" H 4400 1850 50  0001 C CNN
	1    4400 1850
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C3
U 1 1 5E47DD78
P 5000 3150
F 0 "C3" V 4771 3150 50  0000 C CNN
F 1 "100n" V 4862 3150 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 5000 3150 50  0001 C CNN
F 3 "~" H 5000 3150 50  0001 C CNN
	1    5000 3150
	0    -1   1    0   
$EndComp
$Comp
L Device:D_Zener DZ1
U 1 1 5E4D1CA7
P 7700 4100
F 0 "DZ1" V 7654 4179 50  0000 L CNN
F 1 "3V3" V 7745 4179 50  0000 L CNN
F 2 "Diode_SMD:D_MiniMELF" H 7700 4100 50  0001 C CNN
F 3 "~" H 7700 4100 50  0001 C CNN
	1    7700 4100
	0    1    1    0   
$EndComp
$Comp
L Connector:Conn_01x02_Male J2
U 1 1 5E4A803C
P 1500 3650
F 0 "J2" H 1608 3831 50  0000 C CNN
F 1 "Conn_01x02_Male" H 1608 3740 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 1500 3650 50  0001 C CNN
F 3 "~" H 1500 3650 50  0001 C CNN
	1    1500 3650
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x04_Male J1
U 1 1 5E46412C
P 1500 1650
F 0 "J1" H 1608 1931 50  0000 C CNN
F 1 "Conn_01x04_Male" H 1608 1840 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 1500 1650 50  0001 C CNN
F 3 "~" H 1500 1650 50  0001 C CNN
	1    1500 1650
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x03_Odd_Even J3
U 1 1 5E4809CE
P 7100 1750
F 0 "J3" H 7150 2067 50  0000 C CNN
F 1 "Conn_02x03_Odd_Even" H 7150 1976 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical_SMD" H 7100 1750 50  0001 C CNN
F 3 "~" H 7100 1750 50  0001 C CNN
	1    7100 1750
	1    0    0    -1  
$EndComp
$Comp
L Isolator:CNY17-1 U1
U 1 1 5E4A1EE1
P 2650 3700
F 0 "U1" H 2650 4025 50  0000 C CNN
F 1 "CNY17-1" H 2650 3934 50  0000 C CNN
F 2 "Package_DIP:DIP-6_W7.62mm_Socket_LongPads" H 2650 3700 50  0001 L CNN
F 3 "http://www.vishay.com/docs/83606/cny17.pdf" H 2650 3700 50  0001 L CNN
	1    2650 3700
	1    0    0    -1  
$EndComp
$Comp
L Regulator_Linear:LM1117-3.3 U2
U 1 1 5E46A072
P 3900 1550
F 0 "U2" H 3900 1792 50  0000 C CNN
F 1 "LM1117-3.3" H 3900 1701 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-223-3_TabPin2" H 3900 1550 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm1117.pdf" H 3900 1550 50  0001 C CNN
	1    3900 1550
	1    0    0    -1  
$EndComp
$Comp
L MCU_Microchip_ATtiny:ATtiny10-TS U3
U 1 1 5E465F70
P 5300 4050
F 0 "U3" H 4770 4096 50  0000 R CNN
F 1 "ATtiny10-TS" H 4770 4005 50  0000 R CNN
F 2 "Package_TO_SOT_SMD:SOT-23-6" H 5300 4050 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8127-AVR-8-bit-Microcontroller-ATtiny4-ATtiny5-ATtiny9-ATtiny10_Datasheet.pdf" H 5300 4050 50  0001 C CNN
	1    5300 4050
	1    0    0    -1  
$EndComp
$EndSCHEMATC
