#!/usr/bin/python3
# -*- coding: utf-8  -*-


# https://www.tresfacile.net/le-module-csv-python/
from myLib.scrabble import scrabble
import csv

csvfile = open('aScrabble.csv', 'w' )
writer = csv.writer( csvfile, delimiter=';',  quotechar='"', quoting=csv.QUOTE_NONNUMERIC )


dico = [] 
dico.append( [ 'lette', 'points', 'occurence' ] )
for k in scrabble.keys():
    nbr = scrabble[ k ][ 'nombre' ]
    pts = scrabble[ k ][ 'point' ]
    dico.append( [ k, pts, nbr ] )

dico.append( [ 'toto', 'xxx', 'assdd', [ 1,2,3] ] )


writer.writerows( dico )

csvfile.close()