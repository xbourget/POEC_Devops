#python3 -m unittest

import unittest


liste = ['carotte', 'tomate', 'broccoli', 'poivron','radis','pomme', 'cerise', 'fraise']

nomFichier = 'monjardin.txt'

for i in range ( len(liste) ) : 
    monjardin = liste
    print('legume n°' + str(i) + '->' + monjardin + 'vendu au kg')
    #print( "legume n°{idx:<3d} -> {monjardin:^20s} vendu au kilo({monjardin})".format( idx=i, monjardin=liste ) )
