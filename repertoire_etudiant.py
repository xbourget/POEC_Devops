#!/usr/bin/python3
# -*- coding: utf-8  -*-

import os
import json


listeEtudiant = ['tanguy','jessica','irma','marius','clement','john','christophe','philippe','adil']

repertoireBaseName = 'classe'

if not os.path.exists( repertoireBaseName ) :
    os.mkdir( repertoireBaseName )

for etudiant in listeEtudiant:
    path = repertoireBaseName + '/' + etudiant
    if not os.path.exists(path):
        print("creation de :", path)
        os.mkdir( path )
    else:
        print( path, 'existe déja')

    dico = {"prenom" : etudiant}
    jason = json.dumps( dico )
    fichier = open( path + '/' + 'infos.json', 'w')
    fichier.write(jason)

    fichier.close()


