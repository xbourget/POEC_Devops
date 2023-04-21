#!/usr/bin/python3
# -*- coding: utf-8  -*-

from fermeLib.ferme import Ferme
from fermeLib.pature import Pature
from fermeLib.ressource import Ressource

class Animal()  :

    def __init__(self, nom):
        self.nom = nom
        self.energie = 10
        self.eau = 10

    def lever( self ):
        print( str(self), 'je me lève' )

    def coucher( self ):
        print( str(self), 'je me couche' )

    def manger( self ):
        print( str(self), 'je mange' )
        ressource = Ferme.getRessource( 'eau' )
        self.eau += ressource.consommer( 10 )

    def bouger( self, qteMouvement ):
        print( str(self), 'je bouge' )
        self.eau -= qteMouvement
        self.energie -= qteMouvement

    def __str__( self ):
        return "{0} {1}litres {2}calories".format(self.nom, self.eau, self.energie )
