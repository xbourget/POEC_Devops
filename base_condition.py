#!/usr/bin/python3
# -*- coding: utf-8  -*-


#  [ ]

age = 17

if age >= 18 :
    print( 'majeur' )
else:
    print( 'majeur' )


if age >= 50 :
    print( 'retraité' )
elif age > 30 :
    print( 'travailleur' )
else :
    print( 'apprenant' )



legumes =   [ 'rutabaga', 'patate', 'navet', 'poireau', 'choux', 'carotte',  'topinanbour' ]
fruits =    [ 'abricot', 'tomate', 'poire', 'ananas', 'fraise', 'citrouille' ]

panier =    [ 'haricot', 'patate', 'abricot', 'topinanbour', 'laitue' ]

for article in panier :
    if article in legumes:
        print( article, ' -> ',  'legume')
    elif article in fruits:
        print( article, ' -> ','fruit')
    else :
        print( article, ' -> ',"je ne sais pas" )

print( "x" * 19 + " break" )

for article in legumes:
    if article[ -1 ] == 'x' :
        break
    print( article, ' miam ' )

print( "x" * 19 + " continue " )

for article in legumes:
    if article[ -1 ] == 'x' :
        continue
    print( article, ' miam ' )