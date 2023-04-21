#!/usr/bin/python3
# -*- coding: utf-8  -*-


from fermeLib.animal import Animal
from fermeLib.ferme import Ferme

class Cheval( Animal )  :

    def __str__( self ):
        return 'je suis le cheval ' + super().__str__()
    
    def manger( self ):
        if self.isVivant() :
            super().manger()
            ressource = Ferme.getRessource( 'avoine' )
            self.energie += ressource.consommer( 10 )

    def bouger( self, qteMouvement ):
        if self.isVivant() :
            super().bouger( qteMouvement * 1.5, 'je galope'  )
