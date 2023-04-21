#!/usr/bin/python3
# -*- coding: utf-8  -*-


from fermeLib.animal import Animal
from fermeLib.ferme import Ferme

class Chien( Animal )  :

    def __str__( self ):
        return 'je suis le chien ' + super().__str__()
    
    def manger( self ):
        if self.isVivant() :
            super().manger()
            try:
                ressource = Ferme.getRessource( 'viande' )
                self.energie += ressource.consommer( 10 )
            except :
                print( 'pas de viande' )