#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]

from myLib.librairieScrabble import calcScrabble 

ficNameIN = 'legumes.txt'
ficNameOUT = 'legumes.cpy'

fichierLecture = open( ficName )

i = 8
for ligne in fichierLecture :
    print( ligne )

print( '*-*-' * 20 )
fichierLecture.seek( 0, 0)

data = fichierLecture.read()

print( data )

fichierLecture.close()
fichierEcriture.close()
