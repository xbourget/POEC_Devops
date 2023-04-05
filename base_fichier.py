#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


ficName = 'base_liste.py'


legumes =   [ 'rutabaga', 'patate', 'navet', 'poireau', 'choux', 'carotte',  'topinanbour', 'coriandre' , 'ail', 'persil']

fichierEcriture = open( 'legumes.txt', 'w' )

for legume in legumes :
    fichierEcriture.writelines( legume + "\n"  )
    #fichierEcriture.write( chr(10)  )

fichierEcriture.close()