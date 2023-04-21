#!/usr/bin/python3
# -*- coding: utf-8  -*-

import os
import subprocess

process = subprocess.Popen( ['ping', '-c 10', 'google.com'], 
                            stdout=subprocess.PIPE)

process2 = subprocess.Popen( ['grep', '13'],
                            stdin   = process.stdout,
                            stdout=subprocess.PIPE)

while True:
    output = process.stdout2.readline()
    print('xxx', output.strip().decode())
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output 
        #for output in process.stdout.readlines():
        #    print( 'zzz', output.strip())
        break
