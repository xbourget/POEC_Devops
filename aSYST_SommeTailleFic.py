#!/usr/bin/python3
# -*- coding: utf-8  -*-

#import os
import os 
from pathlib import Path

currentPath = os.getcwd()
listFichier =  os.listdir() 

somme = 0
for fic in listFichier:
    fic = currentPath + '/' + fic
    p = Path( fic )
    if p.is_dir() == False:
        taille = Path(fic).stat().st_size
        somme += taille 
        print( fic, taille )
    else:
        print( fic, 'dir')
print( somme )