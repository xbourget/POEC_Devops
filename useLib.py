#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


# les tests se lancent avec cette commande 
#python3 -m unittest base_TemplateProgramme.py


# importation de la librairie des testUnitaires
from myLib.librairieMAJ import setMaj  
from myLib.scrabble import calcScrabble 



nom = 'toto'

print( calcScrabble( 'toto' ) )
print( calcScrabble( 'Wahid' ) )
print( calcScrabble( '123' ) )

try:
    print( calcScrabble( 'toto1' ) )
except Exception as e:
    print( 'contacter')

