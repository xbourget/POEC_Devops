#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


ficNameIN = 'legumes.txt'
ficNameOUT = 'legumes.cpy'

fichierLecture = open( ficNameIN )
fichierEcriture = open(ficNameOUT, "w")

for ligne in fichierLecture :
    print( ligne, end='')

fichierEcriture.writelines(ligne)

fichierLecture.close()
fichierEcriture.close()
