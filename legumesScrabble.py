#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


from  myLib.librairieScrabble import calcScrabble

fichierLecture = open( 'legumes.txt' )

for legume in fichierLecture :
    print( legume, end='' )
    print( calcScrabble( legume ) ) 

fichierLecture.close()

