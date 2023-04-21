#!/usr/bin/python3
# -*- coding: utf-8  -*-

from pature import Pature
from ressource import Ressource

class Mouton()  :

    def __init__(self, nom) -> None:
        self.nom = nom
        self.patures = {} 
        self.ressources = {} 

    def lever ( self ):
        print (str(self),'Bonjour, je suis Shawn, vous me conaissez' + self.nom)

    def coucher( self ):
        print (str(self),'Bonne nuit' + self.nom)

    def manger( self ):
        print (str(self),'J\'aime faire des betises' + self.nom)



    