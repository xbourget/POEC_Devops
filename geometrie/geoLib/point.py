#!/usr/bin/python3
# -*- coding: utf-8  -*-


from random import randint

class Point():

    #variable static
    nbrPoint = 0

    def __init__( self, x, y ):
        #variable d'instance
        self.x = x
        self.y = y
        Point.nbrPoint += 1

    def __str__(self):
        return "({0},{1})".format( self.x, self.y)
    
    def surface(self):
        return 0

    



