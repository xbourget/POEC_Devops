#!/usr/bin/python3
# -*- coding: utf-8  -*-


from random import randint
from geoLib.point import Point
from geoLib.figure import Figure

class Rectangle( Figure ):

    def __init__( self, x, y, lar, long ):
        super().__init__( x, y )
        self.lar =  lar
        self.long =  long

    def __str__(self):
        return "Rectangle {0} lar:{1} long:{2}".format( self.point, self.lar, self.long )

    def __hash__(self):
        return  hash( "Rectangle {0} lar:{1} long:{2}".format( self.point, self.lar, self.long ) )

    def __sizeof__(self):
        return  self.lar * self.long

    def surface(self):
        return self.lar * self.long 
    
    @staticmethod
    def calculeSurface( lar, long ):
        return lar * long 

    @classmethod
    def createRectangle( cls, id ):
        print( 'id', id)
        # je cherche les données dans la BDD
        return cls( 10, 45, 3, 800 ) 





