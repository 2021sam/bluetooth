import threading, sub_rfcomm, time, datetime
t1 = None


def start_thread():
	global t1
	print( f'process started: { datetime.datetime.now() }' )
	t1 = threading.Thread( target = sub_rfcomm.process )
	t1.daemon = True
	t1.start()


def blue():
	global t1
	import time, serial
	# ser = serial.Serial( USB_LoRa, 115200, timeout=1)		#	Went global because needed to asynchronously
	try:
		bluetoothSerial	= serial.Serial("/dev/rfcomm0", baudrate=115200, timeout=3 )
		print("bluetooth connected")
		while t1.is_alive():
			s	= bluetoothSerial.readline().decode("utf-8")
			# hex_string = binascii.hexlify(s).decode('utf-8')
			if s:
				# print ( len( s ))
				print( f'[{s}]', end='' )
				if s.strip() == 'cool':
					bluetoothSerial.write(b'Cool Man!')

			string = input('Enter your name:')
			# print('Hello, ' + x)
			sb = bytes(string, 'utf-8')
			bluetoothSerial.write( sb )

	except serial.SerialException as e:
		if e.errno == 2:
			# raise e
			print( f'Error {e.errno}: Serial bluetooth is not connected. ')

	except KeyboardInterrupt:
		print("Quit")


start_thread()
time.sleep( 1 )

while True:
	if not t1.is_alive():
		start_thread()
	time.sleep( 1 )

	if t1.is_alive():
		blue()

	t = 10
	# print(f'Retrying in {t} seconds.')
	time.sleep( t )
