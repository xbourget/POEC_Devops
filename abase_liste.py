#!/usr/bin/python3
# -*- coding: utf-8  -*-

from random import randint 


#int tableau[10][10];



def disBonjourATous( listeJoueurs ):
    for joueur in listeJoueurs:
        if joueur == "" :
            disBonjour(  )
        else:
            disBonjour( joueur )

# AttributeError:


def removeAll( liste, elem ):
    while True :
        try:
            liste.remove( elem )
        except ValueError :
            break

def isNotToto( nom ):
    if nom != 'toto':
        return True
    else:
        return False

def metMAJ( nom ):
    return nom.upper()


joueurs = [ 'jules', 'toto', 'tata', 'titi', "3.14159", 'tutu', 'tete', 'toto', 'tyty', 'toto' ]
#joueurs = set( joueurs )

#newList = list( filter( isNotToto, joueurs ) )

newList = list( filter( lambda x : x != 'toto', joueurs ) )
print( joueurs )
print( newList )

newList = list( map( metMAJ, joueurs ) )
print( joueurs )
print( newList )

nombres = [ randint( 2, 50) for x in range( 1000000 ) ]

newList = list( map( lambda x : x*x, nombres ) )
#print( newList )


"""
print( joueurs   )
print( joueurs[ -2 ]   )
print( joueurs[ 2 : 5 ]   )
print( joueurs[ 0 : -1 : 2 ]   )
print( joueurs[ :: -1 ]   )
"""

for i in range ( len( joueurs)):
    print( i, joueurs[ i ], end=', ' )
print()
print( 'place tutu', joueurs.index( 'tutu' ))

idx=0
while True :
    if 'toto' in joueurs[ idx : -1 ]:
        idx =  joueurs.index( 'toto', idx )
        print( 'place toto', idx )
        idx += 1
    else:
        break
    
joueurs.append( 'Gontrand' )
joueurs.insert( 0, "Sigismond" )
joueurs.insert( 4, "Zorro" )

#removeAll( joueurs, 'toto' )

print( 'x' *  50 )

for i in range ( len( joueurs)):
    print( i, joueurs[ i ], end=', '  )
print()
del joueurs[4]
for i in range ( len( joueurs)):
    print( i, joueurs[ i ], end=', '  )
print()


#elem = joueurs.pop()
elem = joueurs.pop(3)

print( elem )

for i in range ( len( joueurs)):
    print( i, joueurs[ i ], end=', '  )
print()

