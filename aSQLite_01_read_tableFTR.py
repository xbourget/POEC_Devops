#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble
import  json
import sqlite3

try:

    connection = sqlite3.connect('aScrabble.db')
    
    cursor = connection.cursor()

    requete = "SELECT count(*) FROM lettres ;" 


    print(requete)
    cursor.execute( requete ) 
    nb_lettres = cursor.fetchall() 
    print("nombre de lettre : " + str(nb_lettres))

    for i in nb_lettres :
        requete = "SELECT * FROM lettres where lettre <  'R' "
        cursor.execute(requete)
        result = cursor.fetchall()
        
        print(requete)

    for ligne in result :
        lettre = ligne[1]
        points = ligne[2]
        nbr    = ligne[3]
        print("-> {}  {}  {}".format(lettre,points,nbr))


        #print(result)

    print ('X'  * 50)

    requete = "SELECT lettre, points, nombre FROM lettres ;" 
    print(requete)
    cursor.execute( requete ) 
    
    result = cursor.fetchall()
    print(result)

    print ('X'  * 50)
    
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if connection:
        connection.close()
        print("The SQLite connection is closed")


