#!/usr/bin/python3
# -*- coding: utf-8  -*-


from fermeLib.animal import Animal
from fermeLib.ferme import Ferme

class Cheval( Animal )  :

    def __str__( self ):
        return 'je suis le cheval ' + super().__str__()
    
    def manger( self ):
        super().manger()
        ressource = Ferme.getRessource( 'avoine' )
        self.energie += ressource.consommer( 10 )

