#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]

import os
import json

listeEtudiant = [ 'john', 'dylan', 'wahid', 'tanguy', 'adil', 'christophe', 'marius', 'jessica', 'irma', 'philippe',  'clément' ]

repertoireBaseName = 'classe'

if  not os.path.exists( repertoireBaseName ):
    os.mkdir( repertoireBaseName  )

for etudiant in listeEtudiant:
    path = repertoireBaseName + '/' + etudiant
    if  not os.path.exists( path ):
        print( "creation de :", path )
        os.mkdir( path  )
    else:
        print( path, 'existe déjà' )

    dico = { "prenom" : etudiant }
    jason  = json.dumps( dico )
    fichier  =  open(  path + '/' + 'infos.json', 'w'  )
    fichier.write( jason )
    fichier.close()
