sigrok-cli -i bootup_.sr -P uart:baudrate=9600:parity_type=even:format=hex -A uart=tx-data | 
while IFS='' read -r line || [[ -n "$line" ]]; do
	echo -ne "\\x"
	echo -ne "$line"
#	if [[ $line == "83" ]]; then 
#		read -r lin1 
#		read -r lin2 
#		read -r lin3 
#		echo "sendCmd(b'\\x$lin1\\x$lin2\\x$lin3')"; 
#	elif [[ $line == "84" ]]; then 
#		read -r lin1 
#		read -r lin2 
#		read -r lin3 
#		read -r lin4 
#		echo "sendVal(b'\\x$lin1\\x$lin2\\x$lin3\\x$lin4')" 
#	else 
#		echo "ser.write(b'\x$line')"
#	fi 
done
