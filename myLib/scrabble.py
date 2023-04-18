#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


# les tests se lancent avec cette commande 
#python3 -m unittest 




#import unicodedata
from unicodedata import normalize
import unittest 



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
				"Z" : { "point" : 10,  "nombre" :  1 }  	
			} 



def stripAccents(text):
    text = normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)


def comptePoint( mot ):
	pointTotal = 0
	mot = mot.replace( ' ', '')
	for lettre in mot.upper():
		try :
			pointTotal += scrabble[ lettre ][ 'point' ]
		except KeyError :
			pass
			#print( 'lettre inconnue')
			#return 0
	if len(mot) >= 7 :
		pointTotal += 50
	return pointTotal

class TestScrabble( unittest.TestCase ):
	def test_faux_mots(self):
		self.assertEqual( comptePoint(''), 0)
		self.assertEqual( comptePoint('   '), 0)
		self.assertEqual( comptePoint(' 1353  '), 0)
		#self.assertEqual( comptePoint('xwa  2eeee'), 5 )

	def test_mots_courts(self):
		self.assertEqual( comptePoint('aaaaa'), 5 )
		self.assertEqual( comptePoint(' aaaaa'), 5 )
		self.assertEqual( comptePoint(' aaaaax'), 15 )

	def test_mots_longs(self):
		self.assertEqual( comptePoint('aaaaaaa'), 57 )
		self.assertEqual( comptePoint('xwa2eeee'), 75 )


if __name__ == "__main__" :
	print( comptePoint( 'Zorro' ) )
	print( comptePoint( 'Zorro2' ) )
