#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


# les tests se lancent avec cette commande 
#python3 -m unittest base_TemplateProgramme.py


# importation de la librairie des testUnitaires
#from myLib.librairieMAJ import setMaj  
from myLib.scrabble import calcScrabble


nom = 'toto'

#nom = setMaj( nom )

print( nom ) 

mot=input("Saisir le mot :")
print("Le nombre de point du mot :"+ mot + "est : " + str(calcScrabble( mot)))
