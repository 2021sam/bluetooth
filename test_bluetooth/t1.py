import threading, sub_rfcomm, time, datetime
t1 = None

def start_thread():
	global t1
	print( f'process started: { datetime.datetime.now() }' )
	t1 = threading.Thread( target = sub_rfcomm.process )
	t1.daemon = True
	t1.start()

start_thread()
while True:
	z =  t1.is_alive()
	print( z )
	if not z:
		t = 10
		print(f'Retrying in {t} seconds.')
		time.sleep( t )
		start_thread()

	# print('.', end='')
	time.sleep( 1 )
