#python3 -m unittest

import unittest


liste = ['carotte', 'tomate', 'broccoli', 'poivron','radis','pomme', 'cerise', 'fraise']

nomFichier = 'potager.txt'

for i in range ( len(liste) ) : 
    potager = liste
    #print('legume n°' + str(i) + '->' + potager + 'vendu au kg')
    print( "legume n°{idx:<3d} -> {leg:^20s} vendu au kilo({leg})".format ( idx=i, potager = liste) )
