#!/usr/bin/python3
# -*- coding: utf-8  -*-

# les tests se lancent avec cette commande 
# python3 -m unittest 


import unittest 


listeLegume = [ 'patate', 'carotte', 'chicons', 'rutabaga', 'tomates', 'choux', 'navet', 'salade', 'avocat', 'radis', 'courgette', 'poivron', 'melon' ]


nomFichier = 'legumes.data'

file = open(  nomFichier, 'w' )  #handle

for legume in listeLegume:
    data = "{0:20s}".format( legume )
    file.write( data ) 

file.close()



