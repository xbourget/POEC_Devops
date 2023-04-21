#!/usr/bin/python3
# -*- coding: utf-8  -*-


from fermeLib.animal import Animal
from fermeLib.ferme import Ferme
from fermeLib.pature import Pature
from fermeLib.ressource import Ressource

class Vache( Animal )  :

    def __str__( self ):
        return 'je suis la vache ' + super().__str__()
    
    
    def manger( self ):
        super().manger()
        ressource = Ferme.getRessource( 'foin' )
        self.energie += ressource.consommer( 10 )


