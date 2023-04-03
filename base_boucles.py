#!/usr/bin/python3
# -*- coding: utf-8  -*-

def evalOperateur ( toEval ) :
    print( "{0} = {1}".format( toEval, eval(toEval)) )


print( 'x' * 10 + ' for'  )

for a in range( 1, 9):
    print( a )

print( 'x' * 10 + ' while'  )

a = 1
while a < 9 :
    print( a )
    a += 1


print( 'x' * 10 + ' for avec une liste'  )

noms = ['toto', 'tata', 'titi' ]
for nom in noms:
    print( nom )


