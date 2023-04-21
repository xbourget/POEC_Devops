#!/usr/bin/python3
# -*- coding: utf-8  -*-


from myfermeLib.ferme import Ferme
from myfermeLib.pature import Pature
from myfermeLib.ressource import Ressource

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
        ressource = Ferme.getRessource( 'foin' )
        self.energie += ressource.consommer( 10 )
        ressource = Ferme.getRessource( 'eau' )
        self.eau += ressource.consommer( 10 )

    def __str__( self ):
        return 'inconnu'
    




