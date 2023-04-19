#!/usr/bin/python3
# -*- coding: utf-8  -*-

nom = 'Dupont'
prenom = 'Antoine'
age = 22

chaine = "nom : {name:10s} prenom : {firstname:10s}  age : {old:3d} ({name})".format( firstname=prenom, name=nom, old=age )
print( chaine )


chaine = "nom : {name:10s} prenom : {firstname:10s}  age : {old:3d} ({name})".format( firstname=prenom, name=nom, old=3 )
print( chaine )

chaine = "nom : {name:10s} prenom : {firstname:10s}  age : {old:3d} ({name})".format( firstname=prenom, name=nom, old=100 )
print( chaine )
