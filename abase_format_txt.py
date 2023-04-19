#!/usr/bin/python3
# -*- coding: utf-8  -*-

# les tests se lancent avec cette commande 
# python3 -m unittest 


listeLegume = [ 'patate', 'carotte', 'chicons', 'rutabaga', 'tomates', 'choux', 'navet', 'salade', 'avocat', 'radis', 'courgette', 'poivron', 'melon' ]



for i in range( len(listeLegume) ):
    legume = listeLegume[i]
    #print( 'legume n° ' + str(i) + ' -> ' + legume + ' vendu au kilo' )
    print( "legume n°{idx:<3d} -> {leg:^20s} vendu au kilo({leg})\t\t chance:{numChance:5.2f}".format( idx=i, leg=legume, numChance =(i**5)/100000    )                                )

