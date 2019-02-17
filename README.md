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

### Sniffed Commands ###
from cmds.csv

cmd => 3 byte<br />
key => 4 byte

|cmd type|key|value|bitfield|cam response|topic|setting|
|--------|---|-----|--------|------------|-----|-------|
|cmd|0x00|0x00|0b0100|IMPL|Colorbars|                        |
|||||||                                                      |
|cmd|0x01|0x00|0b0100|IMPL|Detail|                           |
|||||||                                                      |
|cmd|0x02|0x00|0b0100|IMPL|Autoiris|                         |
|cmd|0x02|0x01|0b0100|IMPL|Autoiris|                         |
|||||||                                                      |
|cmd|0x03|0x00|0b0100|IMPL|White Bal|                        |
|cmd|0x03|0x01|0b0100|IMPL|White Bal|Preset                  |
|cmd|0x03|0x02|0b0100|IMPL|White Bal|A                       |
|cmd|0x03|0x03|0b0100|IMPL|White Bal|B                       |
|cmd|0x03|0x0f|0b0100|IMPL|White Bal|full auto               |
|||||||                                                      |
|cmd|0x06|0x00|0b0110|UNIPLM|Auto White|                     |
|cmd|0x06|0x01|0b0110|IMPL|Auto White|                       |
|||||||                                                      |
|cmd|0x07|0x00|0b0100|IMPL|Gain|0dB                          |
|cmd|0x07|0x01|0b0100|IMPL|Gain|6dB                          |
|cmd|0x07|0x02|0b0100|IMPL|Gain|9dB                          |
|cmd|0x07|0x03|0b0100|IMPL|Gain|12dB                         |
|cmd|0x07|0x04|0b0100|IMPL|Gain|18dB                         |
|cmd|0x07|0x05|0b0100|UNIPLM|Gain|                           |
|cmd|0x07|0x06|0b0100|UNIPLM|Gain|                           |
|cmd|0x07|0x08|0b0100|IMPL|Gain|                             |
|cmd|0x07|0x0a|0b0100|IMPL|Gain|3dB                          |
|cmd|0x07|0x0e|0b0100|UNIPLM|Gain|                           |
|||||||                                                      |
|cmd|0x08|0x00|0b0100|IMPL||                                 |
|cmd|0x08|0x01|0b0100|IMPL||                                 |
|||||||                                                      |
|cmd|0x09|0x00|0b0100|IMPL|Call|                             |
|cmd|0x09|0x01|0b0100|IMPL|Call|                             |
|||||||                                                      |
|cmd|0x0b|0x00|0b0110|UNIPLM||                               |
|||||||                                                      |
|cmd|0x0c|0x00|0b0100|IMPL|Shutter|off                       |
|cmd|0x0c|0x01|0b0100|UNIPLM|Shutter|                        |
|cmd|0x0c|0x02|0b0100|IMPL|Shutter|1/120                     |
|cmd|0x0c|0x03|0b0100|IMPL|Shutter|1/250                     |
|cmd|0x0c|0x04|0b0100|IMPL|Shutter|1/500                     |
|cmd|0x0c|0x05|0b0100|IMPL|Shutter|1/1000                    |
|cmd|0x0c|0x06|0b0100|IMPL|Shutter|1/2000                    |
|cmd|0x0c|0x0f|0b0100|UNIPLM|Shutter|                        |
|||||||                                                      |
|cmd|0x0f|0x00|0b0100|IMPL|black mod|unmod                   |
|cmd|0x0f|0x01|0b0100|IMPL|black mod|stretch                 |
|cmd|0x0f|0x02|0b0100|IMPL|black mod|compress                |
|||||||                                                      |
|cmd|0x1b|0x00|0b0100|UNIPLM||                               |
|cmd|0x1b|0x01|0b0100|UNIPLM||                               |
|||||||                                                      |
|cmd|0x1c|0x00|0b0100|IMPL|Auto Knee|                        |
|||||||                                                      |
|cmd|0x1d|0x00|0b0100|IMPL||                                 |
|||||||                                                      |
|cmd|0x4a|0x00|0b0100|IMPL|DNR|                              |
|||||||                                                      |
|cmd|0x4b|0x00|0b0100|UNIPLM||                               |
|cmd|0x4b|0x01|0b0100|UNIPLM||                               |
|cmd|0x4b|0x02|0b0100|UNIPLM||                               |
|cmd|0x4b|0x0f|0b0100|UNIPLM||                               |
|||||||                                                      |
|cmd|0x4c|0x00|0b0100|IMPL||                                 |
|cmd|0x4c|0x01|0b0100|IMPL||                                 |
|cmd|0x4c|0x02|0b0100|IMPL||                                 |
|cmd|0x4c|0x0f|0b0100|UNIPLM||                               |
|||||||                                                      |
|cmd|0x4d|0x00|0b0100|IMPL|Skin Detail|                      |
|||||||                                                      |
|cmd|0x4e|0x01|0b0100|UNIPLM||                               |
|||||||                                                      |
|cmd|0x4f|0x00|0b0100|UNIPLM||                               |
|cmd|0x4f|0x01|0b0100|UNIPLM||                               |
|cmd|0x4f|0x02|0b0100|UNIPLM||                               |
|||||||                                                      |
|cmd|0x50|0x01|0b0100|IMPL||                                 |
|||||||                                                      |
|cmd|0x51|0x00|0b0100|UNIPLM||                               |
|cmd|0x51|0x01|0b0100|UNIPLM||                               |
|||||||                                                      |
|cmd|0x52|0x00|0b0100|IMPL||                                 |
|||||||                                                      |
|cmd|0x53|0x00|0b0100|IMPL||                                 |
|cmd|0x53|0x01|0b0100|IMPL||                                 |
|||||||                                                      |
|cmd|0x7d|0x01|0b0100|IMPL||                                 |
|||||||                                                      |
|key|0x00|0x340||IMPL|Iris|                                  |
|||||||                                                      |
|key|0x02|0x33c||IMPL||                                      |
|||||||                                                      |
|key|0x03|0x368||IMPL||                                      |
|||||||                                                      |
|key|0x06|0x310||IMPL|Black|                                 |
|||||||                                                      |
|key|0x12|0x530||UNIPLM||                                    |
|||||||                                                      |
|key|0x14|0x400||IMPL||                                      |
|||||||                                                      |
|key|0x16|0x400||IMPL||                                      |
|||||||                                                      |
|key|0x26|0x328||IMPL|Red|                                   |
|key|0x26|0x404||IMPL|Red|                                   |
|||||||                                                      |
|key|0x27|0x230||IMPL|Blue|                                  |
|key|0x27|0x41c||IMPL|Blue|                                  |
|||||||                                                      |
|key|0x32|0x604||IMPL||                                      |
|||||||                                                      |
|key|0x36|0x114||IMPL||                                      |
|||||||                                                      |
|key|0x40|0x340||IMPL|Autoiris|                              |
|||||||                                                      |
|key|0x56|0x26e||UNIPLM||                                    |
|||||||                                                      |
|key|0x74|0x801||UNIPLM||                                    |
|||||||                                                      |
|key|0xf2|0x008||UNIPLM||                                    |
|key|0xf2|0x00c||UNIPLM||                                    |
|key|0xf2|0x80c||UNIPLM||                                    |
|||||||                                                      |
|key|0xf3|0x00c||UNIPLM||                                    |
|key|0xf3|0xf7c||UNIPLM||                                    |
