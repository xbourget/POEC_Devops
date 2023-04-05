#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]

from  myLib.librairieScrabble import calcScrabble

ficNameIn = 'legumes.txt'
ficNameOut = 'legumes.copy'
fichierLecture = open( ficNameIn )
fichierEcriture = open(ficNameOut, "w")

i=1
for ligne in fichierLecture:
    print(ligne, end ='')
    fichierEcriture.writelines("{0:3} - {1}" .format(i,ligne), score=calcScrabble(ligne))
    i +=1

for legume in fichierLecture:
    print( legume, end='' )
    print( calcScrabble( legume.strip() ) ) 

fichierLecture.close()
fichierEcriture.close()

