#python3 -m unittest

import unittest
import codecs

liste = ['tomate','pomme', 'cerise', 'fraise','mirtille', 'cassis']

nomFichier = 'monjardin.txt'
file = codecs.open (nomFichier, 'w+', 'utf-8')

file.write("Mon jardin\n")

for i in range ( len(liste) ) : 
    monjardin = liste [i]
    #print('legume n°' + str(i) + '->' + monjardin + 'vendu au kg')
    print( "fruit n°{idx:<3d} ->   {fruit:<20s} vendu au kilo({fruit})".format( idx=i, fruit=monjardin ) )

    file.writelines("fruit n°{idx:<3d} ->   {fruit:<20s} vendu au kilo({fruit})\n".format( idx=i, fruit=monjardin ))

file.close()