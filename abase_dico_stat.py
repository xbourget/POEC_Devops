#!/usr/bin/python3
# -*- coding: utf-8  -*-

from abase_dico_scrabble import calculePoints



texte = """
Si vous donnez aux histoires que vous écrivez à la première personne une vraisemblance telle que 
les gens finissent par y croire, le lecteur pensera presque forcément qu'elles vous sont effectivement arrivées. Ce qui est tout à fait nature lpuisqu', au moment où vous les inventez , il faut bien que vous donniez l'impression qu'elles sont arrivées à celui qui les raconte. Si votre entreprise est réussie, vous amenez celui qui les lit à croire que ces choses là lui sont également arrivées à lui. Le but que vous vous êtes assigné est atteint, 
ou peu s'en faut : créer quelque chose susceptible d'imprégner l'expérience et la mémoire de votre lecteur.
"""

mots = texte.split( )

for mot in mots :
    try : 
        print(mot + ' = ' + str(calculePoints(mot)) + ' points')
    except KeyError :
        print ( mot + ' : lettre inconnu')


"""
occurence = {}

for mot in mots:
    mot = mot.upper()
    if mot in occurence.keys():
        nbr = occurence[ mot ] 
        occurence[ mot ] = nbr + 1
    else : 
        occurence[ mot ] = 1

print( occurence )


for mot in mots:
    mot = mot.upper()
    try:
        occurence[ mot ] += 1
    except KeyError : 
        occurence[ mot ] = 1

print( occurence )

"""





