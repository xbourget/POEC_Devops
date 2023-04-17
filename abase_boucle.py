#!/usr/bin/python3
# -*- coding: utf-8  -*-

from random import randint 


# for( int i=20; i > 10; i -= 2)
for i in range( 20, 10, -2 ) :
    print( i )


joueurs = [ 'toto', 'tata', 'titi', 'tutu', 'tete', 'tyty' ]
for joueur in joueurs :
    if joueur == 'titi' :
        continue
    if joueur == 'tete' :
        break
    print( joueur )


i=0
while i < 50 :
    print( i )
    i += randint(5,20)
