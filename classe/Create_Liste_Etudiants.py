#!/usr/bin/python3
# -*- coding: utf-8  -*-

# Créer un répertoire classe qui contiendra un sous-répertoire au nom de chacun de nous
# A l'intérieur du répertoire de chacun un fichier json avec des infos

import os
import json

Repertoire_Base = '/home/christophe/GIT_Xavier/POEC_Devops/classe/'
Liste_Etudiants = [ 'john', 'dylan', 'marius', 'christophe', 'adil', 'tanguy', 'wahid', 'yann', 'jessica', 'irma', 'philippe', 'clement' ]

# Création des sous-répertoires dans le répertoire classe
for rep in Liste_Etudiants:
    if not os.path.exists(Repertoire_Base+rep) :
        os.mkdir(Repertoire_Base+rep)
    # Création du fichier json contenant tous les prénoms des etudiants
    file = open( Repertoire_Base + rep + '/liste_etudiants.json','a+')
    for prenom in Liste_Etudiants :
        file.writelines( prenom + "\n"  )
    # Fermeture du fichier
    file.close()
