#!/usr/bin/python3
# -*- coding: utf-8  -*-

#import os
import os 

#print( os.listdir() )
try: 
    print( os.rmdir( 'toto') )
    print( os.mkdir( 'toto') )
except :
    pass

print( os.chdir( 'toto') )
print( os.system( 'touch toto1.txt ') )
print( os.chdir( '..') )

print( 's' * 20 )

#stream = os.popen( 'ls -l | grep *.db') 
stream = os.popen( 'ls -l') 
res = stream.read()

"""
print( 's' * 20 )
for i in range ( 10 ):
    res = stream.readline( 50 )
    print( res )
"""
    
"""
print( 's' * 20 )
res = stream.readlines( )
for lig in res :
    print( 'xxx', lig )
"""
print( 's' * 20 )

stream.close()


lignes = res.split( "\n" )
for ligne in lignes:
    print( '>>', ligne)


#print( type(res), res)
resListe    = res.split( )
print( resListe[ -1 ])



