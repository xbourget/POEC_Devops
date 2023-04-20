#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble
import  json
import sqlite3

try:
    """
    connection = mariadb.connect(
        user="db_user",
        password="db_user_passwd",
        host="192.0.2.1",
        port=3306,
        database="employees"
    )
    """

    connection = sqlite3.connect('aScrabble.db')
    
    cursor = connection.cursor()

    requete = """CREATE TABLE IF NOT EXISTS lettres (
	id integer PRIMARY KEY AUTOINCREMENT,
	lettre text NOT NULL,
	points integer,
	nombre integer
    );
    """      
    cursor.execute( requete ) 
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

finally:
    if connection:
        connection.close()
        print("The SQLite connection is closed")


