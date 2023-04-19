#!/usr/bin/python3
# -*- coding: utf-8  -*-

# les tests se lancent avec cette commande 
# python3 -m unittest 


import unittest 

def moyenne( liste ):
    if len( liste ) > 0:
        return somme( liste ) / len( liste )
    raise Exception

def somme( liste ):
	total = 0
	for num in liste:
		total += float( num )
	return total


class TestStat( unittest.TestCase ):
	def test_somme(self):
		self.assertEqual( somme( [] ), 'inf')
		self.assertEqual( somme( [ -10, 10] ), 0)
		self.assertEqual( somme( [5,10,20] ), 35)
		self.assertEqual( somme( [5,"10",20] ), 35)
		self.assertEqual( somme( [5,"XI",20] ), 35)

	def test_moyenne(self):
		self.assertEqual( moyenne( [] ), 0)
		self.assertEqual( moyenne( [ 5, 10, 15] ), 10 )
