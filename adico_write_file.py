#!/usr/bin/python3
# -*- coding: utf-8  -*-

# les tests se lancent avec cette commande 
# python3 -m unittest 


import unittest 


liste = [ 'patate', 'carotte', 'chicons', 'rutabaga', 'tomates', 'choux', 'navet' ]

nomFichier = 'legumes.txt'

file = open(  nomFichier, 'a+' )  #handle

file.writelines( "toto va à la plage\n" )

file.seek( 0 )


text = file.readline()
print( text, end="" )
text = file.readline()
print( text.strip() )

file.close()



