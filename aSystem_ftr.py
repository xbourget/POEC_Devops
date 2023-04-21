#!/usr/bin/python3
# -*- coding: utf-8  -*-

import os
from pathlib import Path 

ListFichier = os.listdir()


currentpath = os.getcwd()
TailleTotal = 0
for fic in ListFichier :
    fic=currentpath+'/'+fic
    p=Path(fic)
    if p.is_dir() == False:
        taille=Path(fic).stat().st_size
        TailleTotal+=taille
        print(fic, taille)
    else : 
        print(fic,'dir')
        

print("taille total : "+str(TailleTotal))



"""
myDirectory = "C:/Users" 
p = Path(myDirectory) 


print(p.is_dir()) # affiche True print(p.is_file()) # affiche False


os.system('ls -lrt')
output = stream.read()

print(output)


stream = os.popen('echo $PATH')

output = stream.read()

print(output)
"""