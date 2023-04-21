#!/usr/bin/python3
# -*- coding: utf-8  -*-

import unittest
from myLib.scrabble import comptePoint, stripAccents
 
text = """
Si vous donnez aux histoires que vous écrivez à la première personne une vraisemblance telle que 
les gens finissent par y croire, le lecteur pensera presque forcément qu'elles vous sont effectivement arrivées.
Ce qui est tout à fait nature puisqu'au moment où vous les inventez , il faut bien que vous donniez l'impression 
qu'elles sont arrivées à celui qui les raconte. Si votre entreprise est réussie, vous amenez celui qui les lit 
à croire que ces choses là lui sont également arrivées à lui. Le but que vous vous êtes assigné est atteint, 
ou peu s'en faut : créer quelque chose susceptible d'imprégner l'expérience et la mémoire de votre lecteur.
"""

text = stripAccents( text.upper().replace('.', ' ' ).replace(',', ' ' ).replace(':', ' ' ).replace( '\'', ' ') )
#print( text )

mots = text.split( )

occurence = {}

for mot in mots:
    try:
        occurence[ mot ] += 1
    except KeyError : 
        occurence[ mot ] = 1

#print( occurence )

for key in occurence.keys():
    point = comptePoint( key )
    occ = occurence[ key ]
    occurence[ key ] = { 'nbr' : occ, 'point' : point  }

print( '+x' * 30 )
#print( occurence )

"""
listeTest = [ 'OU', "L'EXPERIENCE", "PUISQU'AU",  ]
for mot in listeTest:
    print( mot, occurence[ mot ]['nbr'], occurence[ mot ]['point'] )
"""

total = 0
for mot in occurence.keys():
    total += (occurence[ mot ]['point'] * occurence[ mot ]['nbr']) 

print ( total )

class TestScrabble( unittest.TestCase ):
	def test_mo_text(self):
		self.assertEqual( comptePoint( text), 864)