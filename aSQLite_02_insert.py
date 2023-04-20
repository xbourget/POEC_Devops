#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble
import  json
import sqlite3

try:
    connection = sqlite3.connect('aScrabble.db')
    cursor = connection.cursor()

    for k in scrabble.keys():
        nbr = scrabble[ k ][ 'nombre' ]
        pts = scrabble[ k ][ 'point' ]

        #requete = "INSERT INTO lettres (lettre, points, nombre) VALUES ('" + k + "', " + str(pts) + ", " + str(nbr) + ");" 
        requete = "INSERT INTO lettres (lettre, points, nombre) VALUES ( '{0}', {1}, {2} );".format( k, pts, nbr ) 
        
        print( requete ) 
        cursor.execute( requete ) 
        connection.commit()
    
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

finally:
    if connection:
        connection.close()
        print("The SQLite connection is closed")