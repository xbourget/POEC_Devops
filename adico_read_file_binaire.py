#!/usr/bin/python3
# -*- coding: utf-8  -*-

# les tests se lancent avec cette commande 
# python3 -m unittest 

import unittest 

nomFichier = 'legumes.data'

file = open(  nomFichier, 'r' )  #handle

def lecture( num ):
    pos = (num-1) * 20
    file.seek( pos )
    txt = file.read(20)
    print( txt, file.tell() )

lecture( 2 )
lecture( 4 )
lecture( 5 )

file.close()
