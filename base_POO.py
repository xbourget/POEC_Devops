#!/usr/bin/python3
# -*- coding: utf-8  -*-


class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return self.nom + "(" + str(self.age) + ")"


class Etudiant(Personne):
    nbrEtudiant = 0
    def __init__(self, nom, age, niveau):
        super().__init__( nom, age)
        self.niveau = niveau
        Etudiant.nbrEtudiant += 1

    def __str__(self):
        return super().__str__() + " " + self.niveau 

    @staticmethod
    def getNbrEtudiant():
        return Etudiant.nbrEtudiant



p1 = Personne( "Rosemonde", 36)
e1 = Etudiant( "Evariste", 23, "licence M2")

print(p1.nom)
print(p1.age)
print(p1)

print(e1)
print(e1.getNbrEtudiant())
print(Etudiant.getNbrEtudiant())
