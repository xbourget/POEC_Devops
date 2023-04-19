#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble

nomFichier = 'monDico.txt'
file = open(  nomFichier, 'r'  )  #handle


dico = {}

for ligne in file:

    # ligne -> J    8  1

    listeData = ligne.split( ';' ) 
    print( ligne )
    print( listeData )
    lettre  = listeData[ 0 ]
    pts     = int(listeData[ 1 ])
    nbr     = int(listeData[ 2 ])

    dico[ lettre ] = { 'score' : pts, 'nombre' : nbr    }

    sortie = ">> {0:s} -{1:2d} - {2:2d}".format( lettre, pts, nbr   )
    #sortie = lettre + ' ' + str(pts) + ' ' + str(nbr) 
    print( sortie )
    
file.close()

print( dico )
