#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


ficName = 'base_liste.py'

fichierLecture = open( ficName )

for ligne in fichierLecture :
    print( ligne, end='' )

fichierLecture.close()


legumes =   [ 'rutabaga', 'patate', 'navet', 'poireau', 'choux', 'carotte',  'topinanbour' ]
fichierEcriture = open( 'legumes.txt', 'a' )

for legume in legumes :
    fichierEcriture.writelines( legume   )
    fichierEcriture.write( chr(10)  )

fichierEcriture.close()