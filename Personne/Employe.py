#!/usr/bin/python3
# -*- coding: utf-8  -*-


  
class Employe( ):
    def __init__(self, metier):
        self.metier = metier

    def __str__(self):
        return self.metier 

    def __del__(self):
        print(  'je suis le des de EMPLOYE')

