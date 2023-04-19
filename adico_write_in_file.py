#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble

nomFichier = 'monDico.txt'
file = open(  nomFichier, 'w'  )  #handle

for lettre, data in scrabble.items():
    # data -> {'point': 1, 'nombre': 9}
    pts = data[ 'point' ]
    nbr = data[ 'nombre' ]

    sortie = "{0};{1};{2}".format( lettre, pts, nbr   )
    #sortie = lettre + ' ' + str(pts) + ' ' + str(nbr) 
    print( sortie )
    file.writelines( sortie + "\n")

file.close()