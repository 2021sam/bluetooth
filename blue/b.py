import threading, sub_rfcomm

t1 = threading.Thread( target = sub_rfcomm.process )
t1.daemon = True
t1.start()




# https://janakiev.com/blog/python-shell-commands/
import subprocess


def process():
	print('process')
	# sudo rfcomm connect hci0 84:0D:8E:3D:3E:16 1
	process = subprocess.run(['sudo', 'rfcomm', 'connect', 'hci0', '84:0D:8E:3D:3E:15', '1'],
	                           stdout=subprocess.PIPE,
							   stderr=subprocess.PIPE,
							   text=True)

	output = process.stdout
	if output:
		print( f'[{output}]' )

	output = process.stderr
	if output:
		print( f'[{output}]' )


	# Do something else
	return_code = process.returncode
	if return_code is not None:
		print('RETURN CODE', return_code)
		# Process has finished, read rest of the output
		for output in process.stdout:
			print(output)

if __name__ == '__main__':
	process()
