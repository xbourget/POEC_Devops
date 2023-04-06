#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]

from myLib.librairieScrabble import calcScrabble 

ficNameIN = 'legumes.txt'
ficNameOUT = 'legumes.cpy'

fichierLecture  = open( ficNameIN )
fichierEcriture = open( ficNameOUT, "w" )

i = 1
for ligne in fichierLecture :
    ligne = "|{num:>5.2f}|  - |{leg:<30}| |{score:^10d}|".format( num=i*1, leg=ligne[:-1], score=calcScrabble(ligne[:-1]) )
    print( ligne )
    fichierEcriture.writelines( ligne +  "\n" )
    i += 1
fichierLecture.close()
fichierEcriture.close()