#!/usr/bin/python3
# -*- coding: utf-8  -*-

def mulitpli(lim):
    for i in range (1,lim):
        for j in range (1,lim):
        #Façon de formater très utile
            print( " {0:2d} ".format(i*j), end='' )
        print()

mulitpli (3)
multipli (7)