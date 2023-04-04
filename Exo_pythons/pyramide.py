#!/usr/bin/python3
# -*- coding: utf-8  -*-

def pyramide(etagePyramide):
    etoile = "*"
    espace = " "
    nbEspace = espace * (etagePyramide - 1)
    
        for j in range (nbEspace):
            for i  in etagePyramide:
                n=2
                print (nbEspace + "*" * n)
                n = n + 2
