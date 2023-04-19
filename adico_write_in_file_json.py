#!/usr/bin/python3
# -*- coding: utf-8  -*-

from myLib.scrabble import scrabble
import  json

nomFichier = 'monDico.json'
file = open(  nomFichier, 'w'  )  #handle
json.dump( scrabble, file )
file.close()
