#!/usr/bin/python3
# -*- coding: utf-8  -*-

from random import randint 


def tireDesDe( nbr ):
    for i in range( nbr ):
        print( tirageDe(), end = " " )
    print()
    print()
        
def tirageDe( ):
    return randint( 1, 6)

#for i in range(4):
#    print( tirageDe() )


tireDesDe( randint( 5, 10 ) )

