#!/usr/bin/python3
# -*- coding: utf-8  -*-


from fermeLib.animal import Animal
from fermeLib.ferme import Ferme

class Mouton( Animal )  :

    def __str__( self ):
        return 'je suis le mouton ' + super().__str__()
    
    def manger( self ):
        if self.isVivant() :
            super().manger()
            ressource = Ferme.getRessource( 'foin' )
            self.energie += ressource.consommer( 5 )

    def bouger( self, qteMouvement ):
        if self.isVivant() :
            super().bouger( qteMouvement * 0.5, 'je broute'  )

