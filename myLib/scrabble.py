#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


<<<<<<< HEAD
    # les tests se lancent avec cette commande 
#python3 -m unittest base_TemplateProgramme.py

=======
# les tests se lancent avec cette commande 
#python3 -m unittest base_TemplateProgramme.py

import unittest
import unidecode


>>>>>>> bea2ec42a14323b97cceee64b7ed1bc41c763299

scrabble =  { 
				"A" : { "point" :  1,  "nombre" :  9 },  
				"B" : { "point" :  3,  "nombre" :  2 },  	
				"C" : { "point" :  3,  "nombre" :  2 },  	
				"D" : { "point" :  2,  "nombre" :  3 },  	
				"E" : { "point" :  1,  "nombre" : 15 },  	
				"F" : { "point" :  4,  "nombre" :  2 },  	
				"G" : { "point" :  2,  "nombre" :  2 },  
				"H" : { "point" :  4,  "nombre" :  2 },  	
				"I" : { "point" :  1,  "nombre" :  8 },  	
				"J" : { "point" :  8,  "nombre" :  1 },  	
				"K" : { "point" : 10,  "nombre" :  1 },  	
				"L" : { "point" :  1,  "nombre" :  5 },  	
				"M" : { "point" :  2,  "nombre" :  3 },  	
				"N" : { "point" :  1,  "nombre" :  6 },  	
				"O" : { "point" :  1,  "nombre" :  6 },  	
				"P" : { "point" :  3,  "nombre" :  2 },  	
				"Q" : { "point" :  8,  "nombre" :  1 },  	
				"R" : { "point" :  1,  "nombre" :  6 },  	
				"S" : { "point" :  1,  "nombre" :  6 },  	
				"T" : { "point" :  1,  "nombre" :  6 },  	
				"U" : { "point" :  1,  "nombre" :  6 },  	
				"V" : { "point" :  4,  "nombre" :  2 },  	
				"W" : { "point" : 10,  "nombre" :  1 },  	
				"X" : { "point" : 10,  "nombre" :  1 },  	
				"Y" : { "point" : 10,  "nombre" :  1 },  	
				"Z" : { "point" : 10,  "nombre" :  1 },  	
				"*" : { "point" :  0,  "nombre" :  2 }
			} 

<<<<<<< HEAD
mot = 'toto'

pointTotal = 0
for lettre in mot.upper():
    pointTotal += scrabble[ lettre ][ 'point' ]

print( pointTotal)

print ( "xx**xx" * 5 + "  Code de Christophe  " + "xx**xx" * 5 )
print("Installation de pip install unidecode indispensable")

from unidecode import unidecode

def calcScrabble( string) :
    # si le mot comporte des accents, je les transforme en lettres sans accents
	# si le mot comporte des espaces ou des chiffres, tu sors
    string = unidecode( string )
    print ( string )
    string = string.strip()
    print ( string )
	# si le mot comporte plus de lettres qu\'il n'en existe dans le jeu, tu sors
	
    total_count=0
    for lettres in string.upper() :	
        

        total_count += scrabble[ lettres ][ 'point' ] 
    print ( "total_count : " + str( total_count ) )

calcScrabble( "Pé pé" )

#python3 -m unittest
=======

def calcScrabble( string ):
	pointTotal = 0
	string = unidecode.unidecode( string )
	for lettre in string.upper():
		if lettre in scrabble.keys():
			pointTotal += scrabble[ lettre ][ 'point' ]
	return pointTotal

class MyTest( unittest.TestCase ):

	def test_vide( self ):
		self.assertEqual( calcScrabble( ''),  0)

	def test_aaaa( self ):
		self.assertEqual( calcScrabble( 'aaaa'),  4 )

	def test_123( self ):
		self.assertEqual( calcScrabble( '123'),  0 )

	def test_123( self ):
		self.assertEqual( calcScrabble( 'é'), 1  )





if __name__ == '__main__' :
	print ( 'hello toto ')
	print( calcScrabble( '123' ) )

>>>>>>> bea2ec42a14323b97cceee64b7ed1bc41c763299
