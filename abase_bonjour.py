#!/usr/bin/python3
# -*- coding: utf-8  -*-

from random import randint 


def disBonjourATous( listeJoueurs ):
    for joueur in listeJoueurs:
        if joueur == "" :
            disBonjour(  )
        else:
            disBonjour( joueur )

# AttributeError:


def disBonjour( nom = "toi" ):
    nom = str( nom )
    print( 'bonjour ', nom.upper() )



joueurs = [ 'toto', 'tata', 'titi', 3.14159, 'tutu', 'tete', 'toto', 'tyty' ]
#joueurs = set( joueurs )


joueurs.append( 'Gontrand' )


joueurs.remove( 'titi' )


print( type(joueurs))

disBonjourATous( joueurs )





