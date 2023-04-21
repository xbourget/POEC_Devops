#!/usr/bin/python3
# -*- coding: utf-8  -*-

class Ressource()  :

    def __init__(self, nom, qte, unite) -> None:
        self.nom = nom
        self.quantite = qte
        self.unite = unite

    def consommer( self, qte ):
        if self.quantite > qte :
            self.quantite -= qte
            return qte
        else:
            qte = self.quantite
            self.quantite = 0
            return qte  
        
    def __str__(self):
        return "{0} {1} {2}".format( self.nom, self.quantite, self.unite )

