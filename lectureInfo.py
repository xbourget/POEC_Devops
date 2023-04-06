#!/usr/bin/python3
# -*- coding: utf-8  -*-

import os
import json

from os import listdir
from os.path import isfile, join

listeEtudiant=['dylan','john','']
repertoire='classe'

for entry in os.listdir(repertoire):
    print (entry , type(entry))

    if isfile(repertoire+"/"+entry):
        print('fichier')
    else:
        print('repertory')
        for entry2 in os.listdir(repertoire+"/"+entry):
            print('     file')
        else:
            print('     repertory')

   


for i in listeEtudiant:
    file = open(repertoire + "/infos.json")