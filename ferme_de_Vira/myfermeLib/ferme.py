#!/usr/bin/python3
# -*- coding: utf-8  -*-


from myfermeLib.pature import Pature
from myfermeLib.ressource import Ressource

class Ferme()  :

    patures = {} 
    ressources = {} 

    def __init__(self, nom) -> None:
        self.nom = nom

    def addPature( self, nom, surface  ):
        pature = Pature( nom, surface ) 
        Ferme.patures[ nom ] = pature

    def getPature( self, nom ):
        return Ferme.patures[ nom ]

    def addRessource( self, nom, qte, unite  ):
        ressource = Ressource( nom, qte, unite ) 
        Ferme.ressources[ nom ] = ressource

    def getRessource( nom  ):
        return Ferme.ressources[ nom ]
    
    def getListAnimaux( self ):
        liteElements = []
        for nom in Ferme.patures.keys():
            liteElements += Ferme.patures[ nom ].getListElement()
        return liteElements

    def run( self ):
        listeAnimaux = self.getListAnimaux()
        for i in range( 5 ):

            print( 'aube ... ')
            for animal in listeAnimaux:
                animal.lever()

            print( 'midi ... ')
            for animal in listeAnimaux:
                animal.manger()

            print( 'aurore ... ')
            for animal in listeAnimaux:
                animal.coucher()

            print( 'stock : ')
            for r in Ferme.ressources.keys():
                print( '   ->', Ferme.ressources[ r ] )

            print( '*' * 20 )





