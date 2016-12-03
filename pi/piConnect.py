#!/usr/bin/python

import subprocess

# http://stackoverflow.com/questions/3730964/python-script-execute-commands-in-terminal
output = subprocess.check_output("nmap -sP 192.168.1.0/24", shell=True)
result = {}

# https://www.tutorialspoint.com/python/string_split.htm
# http://stackoverflow.com/questions/5749195/how-can-i-split-and-parse-a-string-in-python
# http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string    
for line in output.split(b'\n'):
    if b'raspberrypi' in line:
        result = line.split(b' ')

ip = ((result[5])[1:-1]).decode()
print('Connecting to ' + ip + ' ...\n')
arg = 'pi@' + ip

# https://docs.python.org/3/library/subprocess.html
subprocess.run(["ssh", arg])



