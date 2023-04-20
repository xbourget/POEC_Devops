#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble
import  json
import sqlite3

try:

    connection = sqlite3.connect('aScrabble.db')
    
    cursor = connection.cursor()
    for key in scrabble.keys():
        nbr = scrabble[key]['nombre']
        pts = scrabble[key]['point']


        requete = "INSERT INTO lettres (lettre,points,nombre) values ('" + key + "' , " + str(pts) + ", " + str(nbr) + " );" 
        print(requete)
        cursor.execute( requete ) 
        connection.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if connection:
        connection.close()
        print("The SQLite connection is closed")


