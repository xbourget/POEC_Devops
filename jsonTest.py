#!/usr/bin/python3
# -*- coding: utf-8  -*-

import json

file= open ('rennes.json')

dico = json.load (file)

print (dico, type(dico))