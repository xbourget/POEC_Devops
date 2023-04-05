#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


ficName = 'dicoCompte.py'

fichierLecture = open( ficName )

for ligne in fichierLecture :
    print( ligne )

print( '*-*-' * 20 )
fichierLecture.seek( 0, 0)

data = fichierLecture.read()

print( data )

fichierLecture.close()
