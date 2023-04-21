#!/usr/bin/python3
# -*- coding: utf-8  -*-

class Pature()  :

    def __init__(self, nom, surface) -> None:
        self.nom = nom
        self.surface = surface
        self.elementDansPature = []

    def addElement( self, animal ):
        self.elementDansPature.append( animal )

    def getListElement( self, animal ):
        return self.elementDansPature
        self.elemsDansPature = []

    def addElement( self, animal ):
        self.elemsDansPature.append( animal )

    def getListElement( self ):
        return self.elemsDansPature

