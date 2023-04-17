#!/usr/bin/python3
# -*- coding: utf-8  -*-

from random import randint 


def disBonjour():
    print( 'bonjour')

def disBonjourMulti( nbr ):
    for i in range( nbr ) :
        print( 'bonjour')

def tirageDe( ):
    return randint( 1, 7)

def additionne( a, b ) :
    return a + b

disBonjour()
disBonjour()

print( '=' * 50  )

disBonjourMulti( 4 )

print( '=' * 50  )

print( tirageDe() )

print( '=' * 50  )

res = additionne( 5, 6)
print( res ) 

