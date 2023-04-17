#!/usr/bin/python3
# -*- coding: utf-8  -*-

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