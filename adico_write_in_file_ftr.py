#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble as tableau

nomFichier = 'monDico.csv'
file = open(  nomFichier, 'w'  )  #handle

# Entete
Entete = "lettre , points , nombre \n"
#print(Entete)
file.writelines(Entete)

for cle in tableau.keys() :
    
    contenu = tableau[cle]
    point = contenu["point"]
    nombre = contenu["nombre"]

    Ligne = "{lettre:^6s} , {points:^6d} , {nbr:^6d} \n".format(lettre=cle ,points=point, nbr=nombre)

 #   print(Ligne)

    file.writelines(Ligne)
    
    
file.close()


