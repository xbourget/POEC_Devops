#!/usr/bin/python3
# -*- coding: utf-8  -*-


for age in range (15,75,10) : 

    if age >= 18 and age < 64 :
        print (age)
        print( 'tu es majeur')
    elif age < 18 :
        print (age)
        print( 'tu es mineur')
    else :
        print (age)
        print( 'tu es à la retraite')

age = 65
permis = True

if age >= 64 :
	print( 'retaite')
	print( 'tu as des réduction' )
	if permis :
	    print( 'tu peux conduire' )
	else:
	    print( 'tu peux conduire une voiture ss permis' )
elif age >= 18 :
	print( 'majeur')
	if permis :
	    print( 'tu peux conduire' )
else :
	print( 'mineur')
	print( 'tu peux conduire un vélo' )

print( '*******' )

