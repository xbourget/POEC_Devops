#!/usr/bin/python3
# -*- coding: utf-8  -*-

#import os
from os import *

system('ls -l')

system( 'cp base_CommandeSystem.py base_CommandeSystem.py.copie')


stream = popen('echo $PATH')
output = stream.read()
print( output )


import subprocess

process = subprocess.Popen(
                            ['echo', 'Hello Toto'],
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE
                          )

stdout, stderr = process.communicate()
print( stdout, stderr )
print( stdout.decode()  )
