#!/usr/bin/python3
# -*- coding: utf-8  -*-

from random import randint 


def tireDesDe( nbr ):
    for i in range( nbr ):
        print( tirageDe() )
        
def tirageDe( ):
    return randint( 1, 6)

#for i in range(4):
#    print( tirageDe() )

tireDesDe( 5 )
print( '--------------')
tireDesDe( 2 )

