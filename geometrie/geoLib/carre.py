#!/usr/bin/python3
# -*- coding: utf-8  -*-


from random import randint
from geoLib.point import Point
from geoLib.figure import Figure

class Carre( Figure ):

    def __init__( self, x, y, cote ):
        super().__init__( x, y )
        self.cote = cote

    def __str__(self):
        return "Carré {0} coté:{1}".format( self.point, self.cote )

    def surface(self):
        return self.cote * self.cote 





