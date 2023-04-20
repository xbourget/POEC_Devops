#!/usr/bin/python3
# -*- coding: utf-8  -*-

from random import randint 



file = open( '/etc/passwd' )
data = file.read()
file.close()

print( data )

lignes = data.split( "\n" )

for i in range( len(lignes) ) :
    ligne = lignes[ i ] 
    print( i, ligne )

print( 'o' * 30 )

print( lignes[ 0 ] ) 
# root:x:0:0:root:/root:/root/bash


ligne = lignes[ 0 ]

elems = ligne.split( ':' ) 
for i in range( len(elems) ) :
    elem = elems[ i ] 
    print( i, elem )

elems[ 5 ] = '/home'

ligne = ":".join( elems )
print( ligne )

print( 'o' * 30 )

eleves = [ 'toto', 'tata', 'titi'  ]

# toto, tata, titi



for nom in eleves:
    print( nom, end=', ' )

print()


for i in range( len(eleves)) :
    if i != (len(eleves)-1):
        print( eleves[i], end=', ' )
    else:
        print( eleves[i]  )

print( ', '.join( eleves))


