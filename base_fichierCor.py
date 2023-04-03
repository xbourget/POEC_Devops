#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


ficName = 'base_liste.py'
fichierLecture = open( ficName )

#fichierLecture.seek(0)

fichierEcriture = open( ficName + '.copie', 'a' )

for ligne in fichierLecture :
    print( ligne, end='' )
    fichierEcriture.writelines(  '>>>' + ligne )
    #fichierEcriture.flush()

fichierLecture.close()
fichierEcriture.close()