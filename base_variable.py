#!/usr/bin/python3
# -*- coding: utf-8  -*-

print( 'x' * 10 + ' chaine'  )

uneChaine  = 'Sigismond va à la mer'

uneChaine, temps, age  = 'Sigismond va à la mer', 'beau', 18

print( uneChaine, end = "\n" )
print( temps, temps )

uneChaine = "Gertrude va à la campagne"
print( uneChaine )

uneChaine = """Brieuc va à la ville
Il flâne au marché
et 
achète 6 oeufs.
"""
print( uneChaine )



uneChaine = uneChaine + ' Pour faire une omelette.'  
print( uneChaine )

uneChaine = uneChaine.replace( 'Brieuc', "Célestin" )

print( uneChaine )


a = str( 12 ) 
print( a, type( a ) )
a = str( 0.016 ) 
a =  "0.016" 
print( a, type( a ) )




print( 'x' * 10 + ' entier'  )

unNombre = 21
print( unNombre, type( unNombre ) )


a = int( "12" ) 
print( a, type( a ) )

a = int( 16 )
print( a, type( a ) )

a = int( 11.016 ) 
print( a, type( a ) )

#a = int( "14.18" ) 
a = int( "1418" ) 
print( a, type( a ) )



print( 'x' * 10 + ' réelle'  )


unNombre = 3.14159
print( unNombre, type( unNombre ) )

a = float( 12 ) 
print( a, type( a ) )
a = float( 0.016 ) 
print( a, type( a ) )
a = float( "1418" ) 
print( a, type( a ) )

a = float( "14.18" ) 
print( a, type( a ) )


a = int( 11 ) 
print( a, type( a ) )

a = int( 11.0 ) * 1.0 
print( a, type( a ) )
