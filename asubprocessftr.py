#!/usr/bin/python3
# -*- coding: utf-8  -*-


import subprocess
import os
process = subprocess.Popen(["ping","www.google.com" ],stdout=subprocess.PIPE)

#stdout = process.communicate()

while True:
    output =  process.stdout.readline()
    print('xxx',output.strip())
    return_code = process.poll()
    if return_code is not None:
        print('Retrun Code ',return_code)
        break



print(stdout,stderr)


print(stdout.decode())

