#!/usr/bin/python3
# -*- coding: utf-8  -*-


from abc import abstractmethod, ABC
from random import randint
from geoLib.point import Point

class Figure(ABC):

    def __init__( self, x, y ):
        self.point = Point( x, y )

    def __str__(self):
        return "Figure non défini {0}".format( self.point )

    def __add__(self, fig):
        return self.surface() + fig.surface()

    @abstractmethod
    def surface(self):
        pass
