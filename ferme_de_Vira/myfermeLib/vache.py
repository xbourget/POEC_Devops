#!/usr/bin/python3
# -*- coding: utf-8  -*-


from myfermeLib.animal import Animal
from myfermeLib.ferme import Ferme
from myfermeLib.pature import Pature
from myfermeLib.ressource import Ressource

class Vache( Animal )  :

    def __str__( self ):
        return 'Je suis Milka, j\'habite dans les Alpes ' + self.nom
    
        if self.isVivant() :
            super().manger()
            ressource = Ferme.getRessource( 'foin' )
            self.energie += ressource.consommer( 5 )

    def bouger( self, qteMouvement ):
        if self.isVivant() :
            super().bouger( qteMouvement * 0.5, 'je cours'  )



