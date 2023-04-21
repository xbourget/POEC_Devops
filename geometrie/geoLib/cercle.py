#!/usr/bin/python3
# -*- coding: utf-8  -*-


from random import randint
from geoLib.point import Point
from geoLib.figure import Figure

class Cercle( Figure ):

    PI = 3.14159

    def __init__( self, x, y, rayon ):
        super().__init__( x, y )
        self.rayon = rayon

    def __str__(self):
        return "Cercle {0} rayon:{1}".format( self.point, self.rayon )

    def surface(self):
        return self.rayon * self.rayon * 3.14159 





