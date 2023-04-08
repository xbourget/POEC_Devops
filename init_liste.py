#!/usr/bin/python3
# -*- coding: utf-8  -*-


import random


liste = [] 
dico = { }
for i in range( 100 ): 
    dico[ i ] = random.randint( 1, 50 ) 

for i in range( 100 ): 
    liste.append( random.randint( 1, 50 ) ) 



liste3 = [   x for x in range(100)  if x > 50]
print( liste3 ) 



23200431