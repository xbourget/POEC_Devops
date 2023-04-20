#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble
import  json
import sqlite3

try:
    connection = sqlite3.connect('aScrabble.db')
    cursor = connection.cursor()

    requete = "SELECT count(*) FROM lettres ;" 
    print( requete ) 
    cursor.execute( requete ) 
    resultat = cursor.fetchone()
    print( resultat )

    print( 'x' * 20 )

    requete = "SELECT * FROM lettres WHERE points > 1;" 
    print( requete ) 
    cursor.execute( requete ) 
    resultat = cursor.fetchall()
    print( resultat )

    print( 'x' * 20 )

    requete = "SELECT * FROM lettres WHERE points > 1 AND nombre >  1 OR  lettre = 'X';" 
    print( requete ) 
    cursor.execute( requete ) 
    resultat =  cursor.fetchall( )
    for ligne in resultat:
        lettre  = ligne[ 1 ]
        points  = ligne[ 2 ]
        nbr     = ligne[ 3 ]
        print( "-> {0}  {1}  {2}".format( lettre, points, nbr)  )

    requete = "SELECT count(*) FROM lettres WHERE points > 1 AND nombre >  1;" 
    print( requete ) 
    cursor.execute( requete ) 
    resultat =  cursor.fetchone( )
    print( resultat )
    print( 'nbr lettres rares ', resultat[0] )

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

finally:
    if connection:
        connection.close()
        print("The SQLite connection is closed")