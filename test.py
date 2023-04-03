#!/usr/bin/python3
# -*- coding: utf-8  -*-

a = 5
print( id(a))
a = 'toto'
print( id(a))
b = a
print( b )
print( id(a))
b =  5 
print( b )
print( id(a))
for a in range ( 10 ) :
    print( a )
    print( a * a )

print( 'fin' )  

