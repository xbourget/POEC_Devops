#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


# les tests se lancent avec cette commande 
#python3 -m unittest base_TemplateProgramme.py


# importation de la librairie des testUnitaires
import unittest


# fonction à tester
def setMaj( string ):
    return string.upper()


# class des tests unitaires
class TestAdd(unittest.TestCase):
    def test_setMaj_vide(self):
        self.assertEqual( setMaj(''), '')
    
    def test_setMaj_digit(self):
        self.assertEqual( setMaj('123'), '123')
    
    def test_setMaj_accent(self):
        self.assertEqual( setMaj('éèàù'), 'ÉÈÀÙ')
    


# cette section est lancée uniquement si ce programme est lui-même lancé
# il n'est pas éxécuté si il est pappelé en tant que librairie
if __name__ == "__main__":
    print( 'je peux tester ici')

    if setMaj( 'toto' ) == 'TOTO' :
        print( 'test OK')
    else :
        print( 'test KO')

    
    
