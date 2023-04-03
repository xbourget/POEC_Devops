#!/usr/bin/python3
# -*- coding: utf-8  -*-

def bonjour1 ( prenom ) :
    print( "bonjour " + prenom  )

def bonjour2 ( prenom, nom ) :
    print( "bonjour " + prenom + ' ' + nom )

def bonjour3 ( prenom, nom='' ) :
    print( "bonjour " + prenom + ' ' + nom )

bonjour1( 'toto' )
bonjour2( 'toto', 'dupont' )
bonjour3( 'toto', 'dupont' )
bonjour3( 'toto' )


def additione( a, b ) :
    return a + b

print( additione( 5, 3 )  )

































"""
def pyramide( n ):
    for y in range( 0, n ):
        print( ' ' * (n-y), '*' * (y+1) * 2 )

pyramide( 5 )"""