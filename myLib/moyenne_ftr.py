#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


# les tests se lancent avec cette commande 
#python3 -m unittest 


import unittest 


def moyenne( liste ):
    if(len(liste)> 0 ) : 
        nb_chiffre = 0
        for nb in liste: 
            try :
                if nb is not None and float(nb) > 0 : 
                    nb_chiffre += 1
            except ValueError : 
                pass
        return somme(liste)/nb_chiffre
    else :  return None


def somme( liste ): 
    if(len(liste)> 0 ) : 
        total = 0
        for nb in liste: 
            try :
                if nb is not None and float(nb) > 0 :
                    total += float(nb)          
            except ValueError : 
                 pass
        return total
    else :  return None
     

liste = ['A',None,'Bidule',5,10,15,'20',10.5,-5,'13/2',12/2]

print("liste            : " + str(liste)) 

print("Somme de liste   : " + str(somme(liste)))  

print("moyenne de liste : " +  str(moyenne(liste)))



class TestStat( unittest.TestCase ):
        
    def test_somme(self):
        self.assertEqual( somme( [] ), None )
        self.assertEqual( somme( [5,10,20] ), 35)
        self.assertEqual( somme( [5,"10",20] ), 35)        
        self.assertEqual( somme( [5,"10",-5] ), 15)        

    def test_moyenne(self):
        self.assertEqual( moyenne( [] ), None)
        self.assertEqual( moyenne( [ 5, 10, 15] ), 10 )
