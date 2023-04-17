#!/usr/bin/python3
# -*- coding: utf-8  -*-

print( "x" * 19 + " les listes" )

noms = [ 'toto', 'tata', 'titi', 'tutu', 'tete', 'tyty' ]

print( noms  )
print( noms[ 0 ]  )
print( noms[ 2:4 ]  )
print( noms[ 2: ]  )
print( noms[ -1 ]  )
print( noms[ -2 ]  )
print( noms[ -2: ]  )
print( noms[ :: 2 ]  )
print( noms[ ::-1]  )

nom = 'philomène'

print( nom  )
print( nom[ 0 ]  )
print( nom[ 2:3 ]  )
print( nom[ 2: ]  )
print( nom[ -1 ]  )
print( nom[ :: 2 ]  )
print( nom[ ::-1 ])


print( "x" * 19 + " les opérations sur les listes" )

print(  len( noms )  )
print(  len( nom )  )

noms.append( "dudu" )
print( noms )

unNom = noms.pop()
print( noms )
print( unNom )

noms.insert( 0, 'dodo')

print( noms )
noms.insert( len( noms ), 'dudu')
print( noms )
noms.insert( len( noms )//2, 'didi')
print( noms )
noms.remove( 'didi')
print( noms )
#noms = noms[:len( noms )//2] + 'didi' + noms[len( noms )//2:] 
noms = noms[  :len( noms )//2] + ['didi'] + noms[len( noms )//2:] 
noms.insert( 0, 'didi') 
print( noms )
print(  noms.count( 'didi')  )
pos =  noms.index( 'didi') 
print( pos, noms.index( 'didi', pos+1) )
noms.sort()
print( noms  )


def majuscule( string ):
    return string.upper()

listMaj = list( map( majuscule, noms  )) 
print( listMaj  )

# version lambda

listMaj = list( map( lambda n: n.upper(), noms  )) 
print( listMaj )

listD = list( filter( lambda nom: nom[0] == 'd', noms  )) 
print( listD )

#noms.insert( len( noms ), 3.14 )
#print( noms )

