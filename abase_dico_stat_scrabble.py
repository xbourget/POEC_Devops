#!/usr/bin/python3
# -*- coding: utf-8  -*-

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
print( text )
print( '+x' * 30 )

mots = text.split( )

occurence = {}

for mot in mots:
    try:
        occurence[ mot ] += 1
    except KeyError : 
        occurence[ mot ] = 1

print( occurence )

for key in occurence.keys():
    point = comptePoint( key )
    occ = occurence[ key ]
    occurence[ key ] = { 'nbr' : occ, 'point' : point  }

print( '+x' * 30 )
#print( occurence )

Total = 0
Total_general = 0
for mot in occurence :
    print( mot, occurence[ mot ]['nbr'], occurence[ mot ]['point'] )
    Total = int(occurence[mot]['nbr'])*int( occurence[ mot ]['point'])
    Total_general += Total
    print ('Total : '+ str(Total) +'\n')


print('TOTAL GENERAL :' + str(Total_general))
