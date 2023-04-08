#!/usr/bin/python3
# -*- coding: utf-8  -*-

from Personne.Personne import Personne 
from Personne.Etudiant import Etudiant 
from Personne.Employe import Employe 



p1 = Personne( "Rosemonde", 36)

print( Personne.nbrPersonnes )
print( p1.nbrPersonnes )


e1 = Etudiant( "Evariste", 23, "licence M2")
e2 = Etudiant( "Evariste", 23, "licence M2")
e3 = Etudiant( "Evariste", 23, "licence M2")

print( Personne.nbrPersonnes )

del e3

print( Personne.nbrPersonnes )

print(p1.nom)
print(p1.age)
print(p1)

print(e1)


emp = Employe( "denoyauteur" )
print( emp )


