#!/usr/bin/python3
# -*- coding: utf-8  -*-


<<<<<<< HEAD:ferme/fermeLib/fermeftr.py
from fermeLib.patureftr import Pature
from fermeLib.ressourceftr import Ressource
=======
from fermeLib.pature import Pature
from fermeLib.ressource import Ressource
>>>>>>> xavier:ferme/fermeLib/ferme.py

class Ferme()  :

    patures = {} 
    ressources = {} 

    def __init__(self, nom) -> None:
        self.nom = nom
<<<<<<< HEAD:ferme/fermeLib/fermeftr.py
        
    def addPature( self, nom, surface  ):
        pature = Pature( nom, surface ) 
        Ferme.pature[ nom ] = pature
=======

    def addPature( self, nom, surface  ):
        pature = Pature( nom, surface ) 
        Ferme.patures[ nom ] = pature
>>>>>>> xavier:ferme/fermeLib/ferme.py

    def getPature( self, nom ):
        return Ferme.patures[ nom ]

    def addRessource( self, nom, qte, unite  ):
        ressource = Ressource( nom, qte, unite ) 
        Ferme.ressources[ nom ] = ressource

    def getRessource( nom  ):
        return Ferme.ressources[ nom ]
    
    def getListAnimaux( self ):
<<<<<<< HEAD:ferme/fermeLib/fermeftr.py
        ListElement[]
        for nom in ferme.patures.keys():

        return ListElement[]


    def run( self ):
      # while True:
      for i in range [1,10]:
            listeAnimaux = getListAnimaux()

=======
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
>>>>>>> xavier:ferme/fermeLib/ferme.py





