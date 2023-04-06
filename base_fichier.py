#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


ficNameIN = 'legumes.txt'
ficNameOUT = 'legumes.cpy'

fichierLecture = open( ficNameIN )
fichierEcriture = open ( ficNameOUT, "w" )

i=1
for ligne in fichierLecture :
    print( ligne, end='' )
    fichierEcriture.writelines( "{0:3d} - {1}".format(i, ligne ))
    i += 1

    fichierEcriture.close()
fichierLecture.close()


legumes =   [ 'rutabaga', 'patate', 'navet', 'poireau', 'choux', 'carotte',  'topinanbour' ]

fichierEcriture = open( 'legumes.txt', 'w' )

for legume in legumes :
    fichierEcriture.writelines( legume + "\n"  )
    #fichierEcriture.write( chr(10)  )

fichierEcriture.close()
