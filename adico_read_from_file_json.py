#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble
import  json

nomFichier = 'monDico.json'
file = open(  nomFichier, 'r'  )  #handle
dico = json.load( file )
file.close()

print( dico[ 'A' ]['point'] )
print( dico[ 'k1' ]['famille']['tata']['age'] )