#!/usr/bin/python3

# -*- coding: utf-8  -*-

#  [ ]


    # les tests se lancent avec cette commande 
#python3 -m unittest base_TemplateProgramme.py

import unittest
import unidecode

text = """
Le diable m'emporte si j'en reconnais un seul ! 
D'où sortent-ils donc, ces bandits-là ? Et, en effet, la colère, la faim, ces deux mois de souffrance et cette débandade enragée au travers des fosses, avaient allongé en mâchoires de bêtes fauves les faces placides houilleurs de Montsou.
"""

occurence = {}

"""
for lettre in text.upper():
    if lettre in occurence.keys():
        occurence[ lettre ] = occurence[ lettre ] + 1
    else:
        occurence[ lettre ] = 1 
"""
for lettre in text.upper():
    try :
        occurence[ lettre ] = occurence[ lettre ] + 1
    except KeyError :
        occurence[ lettre ] = 1 

print( occurence )