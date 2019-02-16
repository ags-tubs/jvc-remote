sigrok-cli -i $1 -P uart:baudrate=9600:parity_type=even:format=hex:rx=CAM:tx=CCU -A uart=tx-data,uart=rx-data > dump_analyse_rxtx
sigrok-cli -i $1 -P uart:baudrate=9600:parity_type=even:format=hex:rx=CAM:tx=CCU -A uart=tx-data > dump_analyse_tx
diff -y dump_analyse_rxtx dump_analyse_tx | sed -r 's/[^ ]* ([0-9A-F]*)/\1/g' | sed -r 's/([0-9A-F]{2})</cam: \1/g' | sed -r 's/([0-9A-F]{2})[0-9A-F]{2}/\1/g'
rm dump_analyse_rxtx
rm dump_analyse_tx
