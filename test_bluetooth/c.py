import time, serial
# ser = serial.Serial( USB_LoRa, 115200, timeout=1)		#	Went global because needed to asynchronously
bluetoothSerial	= serial.Serial("/dev/rfcomm0", baudrate=115200, timeout=5 )

print("bluetooth connected")
try:
	while 1:
		s	= bluetoothSerial.readline().decode("utf-8")
		# hex_string = binascii.hexlify(s).decode('utf-8')
		# for c in s:
		# 	print( ord( c ))
		if s:
			print ( len( s ))
		# print( f'[{s}]'.strip(), end='' )


		# bluetoothSerial.write(b'Whats Up ?\r\n')
		# bluetoothSerial.write(b'hats Up ?\r\n')
		# time.sleep( 1 )

except KeyboardInterrupt:
	print("Quit")
