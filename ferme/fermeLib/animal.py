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
        self.message( 'je me lève' )

    def coucher( self ):
        self.message( 'je me couche' )

    def manger( self ):
        if self.isVivant() :
            self.message(  'je mange' )
            ressource = Ferme.getRessource( 'eau' )
            self.eau += ressource.consommer( 10 )

    def bouger( self, qteMouvement, verbe='je bouge' ):
        if self.isVivant() :
            self.message( verbe )
            self.eau -= qteMouvement
            self.energie -= qteMouvement

    def message( self, msg ):
        if self.isVivant() :
            print( str(self), msg )
        
    def __str__( self ):
        if not self.isVivant() :
            return "{0} mort".format(self.nom )
        else:
            return "{0} {1}litres {2}calories".format(self.nom, self.eau, self.energie )

    def isVivant( self ):
        return self.eau > 0 and self.energie > 0