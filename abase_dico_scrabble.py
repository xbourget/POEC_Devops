#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble as pointTab


def calculePoints( mot ):
    sommePoints = 0
    for lettre in mot.upper():
        sommePoints += pointTab[ lettre ]['point']
    return sommePoints



print( calculePoints( "wagon" ) )f
print( calculePoints( "xylophone" ) )