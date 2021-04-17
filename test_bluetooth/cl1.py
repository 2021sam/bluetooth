import subprocess

with open('test.txt', 'w') as f:
    process = subprocess.Popen(['ls', '-l'], stdout=f)

print( process )
