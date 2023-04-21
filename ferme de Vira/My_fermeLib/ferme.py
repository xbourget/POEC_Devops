#!/usr/bin/python3
# -*- coding: utf-8  -*-


from pature import Pature
from ressource import Ressource

class Ferme()  :

    def __init__(self, nom) -> None:
        self.nom = nom
        self.patures = {} 
        self.ressources = {} 

    def addPature( self, nom, surface  ):
        pature = Pature( nom, surface ) 
        self.pature[ nom ] = pature

    def getPature( self, nom ):
        return self.pature[ nom ]

    def addRessource( self, nom, qte, unite  ):
        ressource = Ressource( nom, qte, unite ) 
        self.ressources[ nom ] = ressource

    def getRessource( self, nom, qte, unite  ):
        return self.ressources[ nom ]
    
    def getListAnnimaux( self ):
        listElements = []
        for nom in self.patures.keys() :   
            listeElements += self.patures[ nom ].getListElement

    def run( self ):
        while True:
            listeAnimaux = self.getListAnnimaux()






