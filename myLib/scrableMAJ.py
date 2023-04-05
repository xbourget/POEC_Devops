#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


# les tests se lancent avec cette commande 
#python3 -m unittest base_TemplateProgramme.py


# importation de la librairie des testUnitaires
import unittest
from scrabble.py import calcScrabble


# fonction à tester
def calcScrabble( mot ):
    return mot.upper()


# class des tests unitaires
class TestScrable( unittest.TestCase ):
    def test_calcScrabble_vide(self):
        self.assertEqual( calcScrabble(''), 0)
    
    def test_calcScrabble_digit(self):
        self.assertEqual( calcScrabble('toto'), 4)
   


