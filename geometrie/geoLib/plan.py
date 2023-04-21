#!/usr/bin/python3
# -*- coding: utf-8  -*-


from random import randint
from geoLib.point import Point

class Plan()  :

    nbrfigure = 0

    def __init__( self ):
        self.figures = [] 

    def addElement( self, figure  ):
        Plan.nbrfigure += 1
        self.figures.append( figure )

    def surface( self  ):
        surface = 0
        for f in self.figures:
            surface += f.surface()
            print( f, f.surface() )
        return surface





