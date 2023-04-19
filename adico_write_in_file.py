#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble as tableau

nomFichier = 'monDico.txt'
file = open(  nomFichier, 'w'  )  #handle

# Entete
Entete = "lettre , points , nombre \n"
print(Entete)
file.writelines(Entete)


for lettre, data in scrabble.items():
    # data -> {'point': 1, 'nombre': 9}
    pts = data[ 'point' ]
    nbr = data[ 'nombre' ]

    sortie = "{0};{1};{2}".format( lettre, pts, nbr   )
    #sortie = lettre + ' ' + str(pts) + ' ' + str(nbr) 
    print( sortie )
    file.writelines( sortie + "\n")


for cle in tableau.keys() :
    
    contenu = tableau[cle]
    point = contenu["point"]
    nombre = contenu["nombre"]

    Ligne = "{lettre:^6s} , {points:^6d} , {nbr:^6d} \n".format(lettre=cle ,points=point, nbr=nombre)

    print(Ligne)

    file.writelines(Ligne)
    
    
file.close()