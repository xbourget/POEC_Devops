#!/usr/bin/python3
# -*- coding: utf-8  -*-

class Ressource()  :

    def __init__(self, nom, qte, unite) -> None:
        self.nom = nom
        self.quantite = qte
        self.unite = unite

    def consomme (self,qte,):
        if (self.quantite > qte ):
            self.quantite -=qte
            return qte
        else : 
            qte_restante = self.quantite
            self.quantite = 0
            print('stock vide')
            return qte_restante
        
    def __str__(self):
        return("il reste : {0} {2} de {1}".format(self.nom,self.quantite,self.unite))