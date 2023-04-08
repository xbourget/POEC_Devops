#!/usr/bin/python3
# -*- coding: utf-8  -*-

class Personne:
    nbrPersonnes = 0

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        Personne.nbrPersonnes += 1 

    def __str__(xxx):
        return xxx.nom + "(" + str(xxx.age) + ")"
    
    def __del__(self):
        Personne.nbrPersonnes -= 1 
        print(  'je suis le des de pers')
