import binascii, serial
bluetoothSerial	= serial.Serial("/dev/rfcomm0", baudrate=115200 )

print("bluetooth connected")
try:
	while 1:
		s	= bluetoothSerial.readline().decode("utf-8")
		# hex_string = binascii.hexlify(s).decode('utf-8')
		print( s, end='' )

except KeyboardInterrupt:
	print("Quit")
