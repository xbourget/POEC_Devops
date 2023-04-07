#!/usr/bin/python3
# -*- coding: utf-8  -*-

from Personne.Personne import Personne
from Personne.Employe import Employe

 
class Etudiant( Personne, Employe ):

    def __init__(self, nom,  age, niveau):
        Personne.__init__( self, nom, age)
        Employe.__init__( self, niveau )

    def __str__(self):
        #return super().__str__()
        return Personne.__str__(self) + " " + Employe.__str__(self) 

    def __del__(self):
        print(  'je suis le des de etudiant')


