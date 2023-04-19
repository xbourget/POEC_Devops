#!/usr/bin/python3
# -*- coding: utf-8  -*-

# les tests se lancent avec cette commande 
# python3 -m unittest 

import unittest 

nomFichier = 'monjardin.txt'

file = open(  nomFichier, 'r'  )  #handle

# fichier texte lu ligne par ligne
#for ligne in file :
#    print( ligne.strip() )

# fichier texte lu d'un bloc

txt = file.read( )
#print( txt, type(txt) )
txt = txt.replace( "\n", ', ')      
print( txt )

print( 'xX' * 50 )

file.seek( 20 )

posCourante = file.tell()

txt = file.read(  )
#print( txt, type(txt) )
txt = txt.replace( "\n", ', ')      
print( txt )


file.close()







