#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


    # les tests se lancent avec cette commande 
#python3 -m unittest base_TemplateProgramme.py


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

mot = 'titanic'



def calcScrable( string ):
	pointTotal = 0
	for lettre in string.upper():
		pointTotal += scrabble[ lettre ][ 'point' ]
	return pointTotal

