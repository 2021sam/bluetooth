import time, serial
# ser = serial.Serial( USB_LoRa, 115200, timeout=1)		#	Went global because needed to asynchronously
try:
	bluetoothSerial	= serial.Serial("/dev/rfcomm0", baudrate=115200, timeout=5 )
	print("bluetooth connected")
	while 1:
		s	= bluetoothSerial.readline().decode("utf-8")
		# hex_string = binascii.hexlify(s).decode('utf-8')
		if s:
			# print ( len( s ))
			print( f'[{s}]', end='' )
			if s.strip() == 'cool':
				bluetoothSerial.write(b'Cool Man!')

		# bluetoothSerial.write(b'Whats Up ?\r\n')
		# bluetoothSerial.write(b'hats Up ?\r\n')
		# time.sleep( 1 )

# except FileNotFoundError as e:
# 	print( e.errno )
# 	raise e
# 	print('Yo dude file not found')

except serial.SerialException as e:
	if e.errno == 2:
		# raise e
		print( f'Error {e.errno}: Serial bluetooth is not connected. ')
		time.sleep( 60 )
		print( 'Auto retry in 60 seconds.')

except KeyboardInterrupt:
	print("Quit")
