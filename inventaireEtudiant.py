#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]

import os
import json

from os.path import isfile, join

repertoireBaseName = 'classe'
            
for entry in os.listdir( repertoireBaseName ): 
    print( entry , type(entry) )
    if isfile( repertoireBaseName + '/' + entry ) :
        print( 'file')
    else:
        print( 'repertory')
        for entry2 in os.listdir( repertoireBaseName + '/' + entry): 
            print( '    ', entry2 , type(entry2) )
            if isfile( repertoireBaseName + '/' + entry + '/' + entry2 ) :
                print( '    file')
            else:
                print( '    repertory')
        





