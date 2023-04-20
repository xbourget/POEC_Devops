#!/usr/bin/python3
# -*- coding: utf-8  -*-

#import os
import os 

print( os.listdir() )

print( 's' * 20 )
os.system('ls -l')

print( 's' * 20 )
os.system( 'touch tototata.txt')

stream = os.popen('echo $VARIABLE')
path = stream.read()
stream.close()

path = path.strip()
print( path )
path += ':/toto' 
print( path )

cmd = 'VARIABLE='+ path
print( cmd )
stream = os.popen( cmd)
#stream = os.popen('touch xxx.txt')
print( stream.read() )
stream.close()

"""


import subprocess

process = subprocess.Popen(
                            ['echo', 'Hello Toto'],
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE
                          )

stdout, stderr = process.communicate()
print( stdout, stderr )
print( stdout.decode()  )
"""