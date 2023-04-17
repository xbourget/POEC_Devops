#!/usr/bin/python3
# -*- coding: utf-8  -*-


import random


liste = [] 
dico = { }
for i in range( 100 ): 
    dico[ i ] = random.randint( 1, 50 ) 


print( dico )

keys = list(dico.keys())
keys.sort()

for i in keys:
    print( dico[ i ] , end=" ")
print()