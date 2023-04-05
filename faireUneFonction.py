#!/usr/bin/python3
# -*- coding: utf-8  -*-

def mutipli( lim ):
    for i in range( 1, lim ):
        for j in range( 1, lim):
            print( "{0:2d} ".format( i*j ) , end='' )
        print()

mutipli( 3 )  
mutipli( 7 )





