#!/usr/bin/python3
# -*- coding: utf-8  -*-

class Pature()  :


    def __init__(self, nom, surface) -> None:
        self.nom = nom
        self.surface = surface
        self.elemeDansPature = []

    def addElement( self, animal ):
        self.elemeDansPature.append( animal )

    def getListElement( self, animal ):
        return self.elemeDansPature

