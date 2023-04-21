#!/usr/bin/python3
# -*- coding: utf-8  -*-


from fermeLib.patureftr import Pature
from fermeLib.ressourceftr import Ressource

class Ferme()  :

    patures = {} 
    ressources = {} 

    def __init__(self, nom) -> None:
        self.nom = nom
        
    def addPature( self, nom, surface  ):
        pature = Pature( nom, surface ) 
        Ferme.pature[ nom ] = pature

    def getPature( self, nom ):
        return self.pature[ nom ]

    def addRessource( self, nom, qte, unite  ):
        ressource = Ressource( nom, qte, unite ) 
        Ferme.ressources[ nom ] = ressource

    def getRessource( self, nom, qte, unite  ):
        return self.ressources[ nom ]
    
    def getListAnimaux( self ):
        ListElement[]
        for nom in Ferme.patures.keys():
            ListElement += Ferme.getListAnimaux()
        return ListElement


"""
    def run( self ):
         # while True:
      
      for i in range [1,10]:
        listeAnimaux = getListAnimaux()

    print ('stock : \n')
    for r in Ferme.ressources.key():
        print('-> il reste {1}'.format(Ferme.get) )

"""


