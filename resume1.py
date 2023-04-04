#!/usr/bin/python3
# -*- coding: utf-8  -*-

# les variables 
uneVariable = 'TOTO'
unNombre = 12
unNombre = 12,23
print( id( unNombre ))
print( type( unNombre ))



print( '-' * 20  ) 
# les chaines


maChaine = [ 12.5, 'toto', 'tulipe', 3.14, 'tata'  ] 

print( maChaine )
print( type( maChaine ))
print( maChaine[ 1 ] )
print( maChaine[ 0:3 ][1] )
print( maChaine[  :3 ] )
print( maChaine[  :-2 ] )
print( maChaine[  :: -1 ] )

print( '-' * 20  ) 

for i in range( 1, 6):
    for j in range( 1, 6):
        print(i, 'x', j, '=', i*j )

for i in range( 1, 6):
    for j in range( 1, 6):
        print( ' ', i*j, end='' )
    print()

for i in range( 1, 6):
    for j in range( 1, 6):
        print( "{0:2d} ".format( i*j ) , end='' )
    print()







