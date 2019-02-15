JVC Remote
==========

### Pinout ###

[26pin_studio_10pin_remote_6pin_tally.xls](cable_doku/26pin_studio_10pin_remote_6pin_tally.xls)

Es wird nur der Remote Anschluß benötigt.<br />
Der Stecker ist ein gewönlicher 6pin Mini-Din (der PS/2 Stecker) Anschluß.<br />
Zum Beispiel: <http://www.reichelt.de/SE-DIO-M06/3/index.html?&ACTION=3&LA=446&ARTICLE=17457&artnr=SE-DIO+M06>

Protokoll
---------

Signallevel: 3.3V<br />
Format: 9600baud 1E8 (8 daten, 1 stop-bit, even-parity)

### Syntax ###

<table >
	<thead>
	<tr >
		<th  colspan="5">  Packet Syntax                                          </th>
	</tr>
	</thead>
	<tr >
		<th >Richtung (von OCP gesehen) </th>
        <td >  TX       </td>
        <td >  RX  </td>
        <td >  TX   </td>
        <td >  RX  </td>
	</tr>
	<tr >
		<th >Länge (in Byte)            </th>
        <td >  1        </td>
        <td >  1   </td>
        <td >  3-4  </td>
        <td >  1   </td>
	</tr>
	<tr >
		<th >Funktion                   </th>
        <td > Startbyte </td>
        <td > ACK  </td>
        <td > Daten </td>
        <td > ACK  </td>
	</tr>
</table>

<table >
	<thead>
	<tr >
		<th  colspan="9">  Startbyte    </th>
	</tr>
	</thead>
	<tr >
		<th > Bit      </th>
<td >  0        </td>
<td >  1  </td>
<td >  2  </td>
<td >  3  </td>
<td >  4  </td>
<td >  5  </td>
<td >  6  </td>
<td >  7  </td>
	</tr>
	<tr >
		<th > Funktion </th>
<td >  immer 1  </td>
<td  colspan="4">  0           </td>
<td  colspan="3">  Länge der Daten    </td>
	</tr>
</table>

<table>
   <tr>
    <th colspan="9">Startbyte</th>
   </tr>
   <tr>
    <th>Bit</th>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
  </tr>
  <tr>
    <th>Funktion</th>
    <td>immer 1</td>
    <td colspan="4">0</td>
    <td colspan="3">Länge der Daten</td>
  </tr>
</table>

4 Byte:

<table >
	<thead>
	<tr >
		<th  colspan="33">  Daten    </th>
	</tr>
	</thead>
	<tr >
		<th > Byte     </th>
        <td  colspan="8">  0  </td>
        <td  colspan="8">  1  </td>
        <td  colspan="8">  2  </td>
        <td  colspan="8">  3  </td>
	</tr>
	<tr >
		<th > Bit      </th>
        <td >  0  </td>
        <td >  1  </td>
        <td >  2  </td>
        <td >  3  </td>
        <td >  4  </td>
        <td >  5  </td>
        <td >  6  </td>
        <td >  7  </td>
        <td >  0  </td>
        <td >  1  </td>
        <td >  2  </td>
        <td >  3  </td>
        <td >  4  </td>
        <td >  5  </td>
        <td >  6  </td>
        <td >  7  </td>
        <td >  0  </td>
        <td >  1  </td>
        <td >  2  </td>
        <td >  3  </td>
        <td >  4  </td>
        <td >  5  </td>
        <td >  6  </td>
        <td >  7  </td>
        <td >  0  </td>
        <td >  1  </td>
        <td >  2  </td>
        <td >  3  </td>
        <td >  4  </td>
        <td >  5  </td>
        <td >  6  </td>
        <td >  7  </td>
	</tr>
	<tr >
		<th > Funktion </th>
        <td  colspan="12">  Funktion  </td>
        <td  colspan="12">  Wert  </td>
        <td  colspan="8">  Prüfsumme  </td>
	</tr>
</table>

3 Byte:


<table >
	<thead>
	<tr >
		<th  colspan="25">  Daten    </th>
	</tr>
	</thead>
	<tr >
		<th > Byte     </th>
        <td  colspan="8">  0  </td>
        <td  colspan="8">  1  </td>
        <td  colspan="8">  2  </td>
	</tr>
	<tr >
		<th > Bit      </th>
        <td >  0  </td>
        <td >  1  </td>
        <td >  2  </td>
        <td >  3  </td>
        <td >  4  </td>
        <td >  5  </td>
        <td >  6  </td>
        <td >  7  </td>
        <td >  0  </td>
        <td >  1  </td>
        <td >  2  </td>
        <td >  3  </td>
        <td >  4  </td>
        <td >  5  </td>
        <td >  6  </td>
        <td >  7  </td>
        <td >  0  </td>
        <td >  1  </td>
        <td >  2  </td>
        <td >  3  </td>
        <td >  4  </td>
        <td >  5  </td>
        <td >  6  </td>
        <td >  7  </td>
	</tr>
	<tr >
		<th > Funktion </th>
        <td  colspan="8">  Funktion  </td>
        <td  colspan="8">  Wert  </td>
        <td  colspan="8">  Prüfsumme  </td>
	</tr>
</table>

                                                                       

### Funktionen ###

|  Funktion      | Packetlänge   | Command-Byte   | Wertebereich
|  ------------- | ------------- | -------------- | ---------------------------------------------------------------------------------------------- |
|  Iris          | 4             | 0              |                                                                                                |
|  Black         | 4             | 6              |                                                                                                |
|  Red           | 4             | 38             |                                                                                                |
|  Blue          | 4             | 39             |                                                                                                |
|  Autoiris      | 4             | 64             | 487547                                                                                         |
|  Auto White    | 3             | 6              |                                                                                                |
|  Colorbars     | 3             | 0              |                                                                                                |
|  Detail        | 3             | 1              |                                                                                                |
|  Autoiris      | 3             | 2              |                                                                                                |
|  White Bal     | 3             | 3              | 1: Preset; 2: A; 3: B 15: full auto                                                            |
|  Auto White    | 3             | 6              |                                                                                                |
|  Gain          | 3             | 7              | 0 : 0dB, 10 : 3dB, 1 : 6dB, 2 : 9dB, 3 : 13dB, 4 : 18dB                                        |
|  Call          | 3             | 9              |                                                                                                |
|  Shutter       | 3             | 12             | 64 : \"off\", 66 : \"1/120\", 67 : \"1/250\", 68 : \"1/500\", 69 : \"1/1000\", 70 : 1/2000\"   |
|  black mod     | 3             | 15             | 0:unmod, 1: stretch, 2: compress                                                               |
|  Auto Knee     | 3             | 28             |                                                                                                |
|  DNR           | 3             | 74             |                                                                                                |
|  Skin Detail   | 3             | 77             |                                                                                                |
                                                                                                                                                |
