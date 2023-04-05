#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


ficNameI = 'legumes.txt'
ficNameO = 'legumesNew.txt'

fichierL = open( ficNameI )
fichierE = open( ficNameO, "w" )

#for ligne in fichierLecture :
#   print( ligne, end='' )
    


#legumes =   [ 'rutabaga', 'patate', 'navet', 'poireau', 'choux', 'carotte',  'topinanbour' ]
#fichierEcriture = open( 'legumes.txt', 'a' )

i=8
for ligne in fichierL :
    print(ligne, end= '')
    fichierE.writelines( "|{0:10d} - {1}\n".format(num=i, leg=ligne[:-1] ))
    i += 1
    #fichierE.write( chr(10)  )


fichierL.close()
fichierE.close()
