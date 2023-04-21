#!/usr/bin/python3
# -*- coding: utf-8  -*-

#import os
import os 
import subprocess



process = subprocess.Popen( [ "cat",  "/etc/passwd" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE   )

stdout, stderr = process.communicate()
print( stdout, stderr )
print( 'x'* 20 )
print( stdout.decode()  )

print( 'x'* 20 )
print( 'x'* 20 )

process = subprocess.Popen( [ "ping",  "google.com" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE   )

stdout, stderr = process.communicate()

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

