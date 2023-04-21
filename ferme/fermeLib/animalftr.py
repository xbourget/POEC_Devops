#!/usr/bin/python3
# -*- coding: utf-8  -*-

from fermeLib.fermeftr import Ferme
from fermeLib.patureftr import Pature
from fermeLib.ressourceftr import Ressource

class Animal():

    def __init__(self, nom) -> None:
        
        self.nom = nom
        self.energie = 10
        self.eau = 10

    def __str__(self) -> str:
        return 'je suis la vache : ' + self.nom       
    
    def lever (self):
        print(str(self),', je me lève')    


    def mangerr (self):
        ressource = Ferme.getRessource('foin')
        self.energie += ressource.consommer('foin',10)
        print(str(self),', je mange')  

    def boire (self):
        ressource = Ferme.getRessource('eau')
        self.eau += ressource.consommer('eau',10)
        print(str(self),', je bois')  
        
    
    def coucher (self):
        print(str(self),', je me couche')    
    
            









