#!/usr/bin/python3
#-*- coding: utf-8 -*-

# les variablles
uneVariable = 'toto'
unNombre = 12
unNombre = 12,23

print( id( unNombre))
print( type( unNombre))

#les listes

maListe= [12.5, 'toto', 'tulipe', 3.14, 'tata' ]
print (maListe)
print (type( maListe))

#Rajouter l'antislash au niveau de '
maChaine = 'supery\'a du soleil'
#Affiche 
print (maListe[ 1:3 ] )
print (maListe[ :: -1])
print (maListe[ :: -1])
print (maListe[ 0:3][1])
print (maListe[ :-2])

#Affiche 20 tirets
print ('-' * 20)

#Ne pas oublier n-1 pour le range 
for i in range(10):
    print(i)
#
for i range (1,6):
    for j in range (1,6):
        print(i, 'x', j, '=', i*j )

for i range (1,6):
    for j in range (1,6):
        print( ' ', i*j, end='' )
    print()

for i range (1,6):
    for j in range (1,6):
        #Façon de formater très utile
        print( " {0:2d} ".format(i*j), end='' )
    print()


def









