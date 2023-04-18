#!/usr/bin/python3
# -*- coding: utf-8  -*-

from random import randint 
from statistics import mean


nom     = 'toto'
age     = 19
poids   = 67.4


def  hello( prenom = "tous" ) :
    print('bonjour ' + prenom )

hello( nom )
hello()


def add( a,  b=0, c=0) :
    return a + b + c

print( add( 8 ) )
print( add( 8, 5 ) )
print( add( 8, 5, 4 ) )
print( add(  c='toto', b=' -> ', a='bonjour' ) )
print( add( 'bonjour ', 'toto', ''  ) )


#print( add( 'bonjour ', 13 ) )

print(  eval( " '3' + '45' "  )   )


def totalPrixTTC( prixHT=0, Qte=1, remise=0, TVA=20 ):
    return ((prixHT*Qte) - remise) * (1+(TVA/100))

def totalPrixTTCDetail( prixHT=0, Qte=1, remise=0, TVA=20 ):
    prixHT = (prixHT*Qte) - remise
    prixTTC = prixHT * (1+(TVA/100))
    return  prixHT, prixTTC

print( totalPrixTTC( 15, 2  )   )

print( totalPrixTTC( 10, TVA=20 )   )

pHT, pTTC = totalPrixTTCDetail( 10, TVA=20 )

print( pHT, pTTC  )


liste = [   4,54,6,5,4,6,54,65,4  ]

def calculeMoySomme(  l ) :
    somme = 0
    for val in l:
        somme += val
    return somme/len(l), somme

def calculeMoySomme2(  l ) :
    return mean(l), sum( l )

print(  calculeMoySomme( liste)   )
print(  calculeMoySomme2( liste)   )

