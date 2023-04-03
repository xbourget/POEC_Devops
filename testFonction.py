#!/usr/bin/python3
# -*- coding: utf-8  -*-




def disBonjourA( prenom = '', nom='' ):
    print( 'bonjour ', prenom, ' ', nom )


disBonjourA()
disBonjourA()
disBonjourA( 'Philippe' )
disBonjourA( 'Philippe', nom='Gertrude'  )
disBonjourA( nom='Philippe', prenom='Gertrude' )
disBonjourA( 3.15, [ 'toto', 'tata' ] )

def additionne ( a, b ):
    return a+b

def calcule ( a, b ):
    return a+b, a*b

a, m = calcule( 5, 3 )
print( a, m)

l = list( calcule( 5, 3 ) )
print( l )

print( additionne( 5, 3), end = "....\n  " )


def moyenne( l ):
    cpt = 0
    sum = 0
    for i in l:
        sum = sum + i
        cpt += 1
    return sum/cpt

def moyenne2( l ):
    return somme(l)/len(l) 

import statistics 

def moyenne3( l ):
    return statistics.mean(l) 


def somme( l ):
    sum = 0
    for i in l:
        sum = sum + i
    return sum

def sommes( l ):
    return sum( l )

l = [ 25, 35  ]
s = somme(  l )
print(s  )





def pyramide( h ):
    for i in range ( 1, h ):
        print( ' ' * ( h-i ), end="")
        print( '**' * i )
        

pyramide( 5 ) 
pyramide( 8 ) 

n = 100000

sum = 0
import time

t = time.time()
print( t  )
for i in range( n ):
    sum += i
    #print( i, end='')
print( sum )

print( time.time() - t )

print( (n-1) * n /2 )

print( time.time() - t )






