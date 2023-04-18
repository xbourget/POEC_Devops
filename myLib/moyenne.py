#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]


# les tests se lancent avec cette commande 
#python3 -m unittest 


import unittest 


def moyenne( liste ):
	return ...

def somme( liste ):
	return ...


class TestStat( unittest.TestCase ):
	def test_somme(self):
		self.assertEqual( somme( [] ), 0)
		self.assertEqual( somme( [5,10,20] ), 35)
		self.assertEqual( somme( [5,"10",20] ), 35)

	def test_moyenne(self):
		self.assertEqual( moyenne( [] ), 0)
		self.assertEqual( moyenne( [ 5, 10, 15] ), 10 )
