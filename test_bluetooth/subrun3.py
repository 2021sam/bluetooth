# https://janakiev.com/blog/python-shell-commands/
import subprocess

# sudo rfcomm connect hci0 84:0D:8E:3D:3E:16 1
# process = subprocess.Popen(['sudo', 'rfcomm', 'connect', 'hci0', '84:0D:8E:3D:3E:16', '1'],

# process = subprocess.run(['sudo', 'rfcomm', 'connect', 'hci0', '84:0D:8E:3D:3E:15', '1'],
#                            stdout=subprocess.PIPE,
#                            universal_newlines=True,
# 						   capture_output=True)



process = subprocess.run(['sudo', 'rfcomm', 'connect', 'hci0', '84:0D:8E:3D:3E:16', '1'],
                           stdout=subprocess.PIPE,
						   text=True)

# while True:
output = process.stdout
print( f'[{output}]' )
# print(f'[{ output.strip() }]')
# print(f'[{ output.decode('utf-8') }]')
# print( output.strip() )
# Do something else
return_code = process.returncode
if return_code is not None:
# if return_code:
    print('RETURN CODE', return_code)
    # Process has finished, read rest of the output
    for output in process.stdout:
        print(output)
    # break
