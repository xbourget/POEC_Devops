#!/usr/bin/python3

# -*- coding: utf-8 -*-


import sqlite3


con = sqlite3.connect("scrabble.db")

cursor = con.cursor()

requete ="CREATE TABLE lettre(nom, points, occurence)"

cursor.execute(requete)


con.close()