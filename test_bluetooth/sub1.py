import subprocess
process = subprocess.Popen(['echo', 'More output'],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print( stdout.decode('utf-8'), stderr.decode('utf-8') )
