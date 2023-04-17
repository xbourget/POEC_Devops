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