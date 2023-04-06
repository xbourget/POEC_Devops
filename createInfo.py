#!/usr/bin/python3
# -*- coding: utf-8  -*-

import os
import json

listeEtudiant=['dylan','john','']

repertoire='classe'

if not os.path.exists ( repertoire):
	os.mkdir(repertoire)

for etudiant in listeEtudiant:
    path=repertoire + '/' + etudiant
    if not os.path.exists( path) :
        print("creation de :", path)
        os.mkdir(path)
        #os.system("touch "+path+"/info.json")
    else:
         print(path, 'existe déjà')
    dico = {"prenom" : etudiant}
    jason =json.dumps(dico)

    with open(path+'/'+'infos.json','w')  as VAR:
         VAR.write(jason)
    
      





