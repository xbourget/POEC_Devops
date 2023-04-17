#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ] |

import json
import psutil
import os
import subprocess

print( json.dumps( psutil.cpu_percent(4) ) )
res = psutil.virtual_memory() 
print( res.total>>30, 'Go' )
print( res.total/(1024*1024*1024), 'Go' )
print( res.total/(1000*1000*1000), 'Go' )
res = str( res )
print( res, type( res ) )

path = "cricKrok1/toto/tata/titi"
#os.makedirs(path)
#subprocess.run(["tree"])
#subprocess.run(["ps", "aux", "|", "grep" , "snap"])
#subprocess.run(["ps", "aux"])
#mycmd=subprocess.getoutput('ps -aux |grep apache2')
#print( mycmd )
p1 = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "apache2"], 
                        stdin=p1.stdout, 
                        stdout=subprocess.PIPE,
                        universal_newlines=True)
#print( '>>', p2 )
#print( '>>', p2.stdout )

p1.stdout.close()

res = str(p2.communicate()[ 0 ])
print( '>>', res )


"""
process = subprocess.Popen(['ping', '-c 4', 'python.org'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

while True:
    output = process.stdout.readline()
    print(output.strip())
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output 
        for output in process.stdout.readlines():
            print(output.strip())
        break
"""
