#!/usr/bin/python3
# -*- coding: utf-8  -*-

import json

classe = { 
              'john'  : { 'nat' : 'eng', "sport" : 'course' },
              'dylan' : { 'nat' : 'bzh', 'music': [ 'jazz', 'blues'], 'cuisine' : 'japonais'  },
              'marius' : { 'pointure' : 45, 'cuisine' : [ 'poisson gri', 'ratatouille']  }
        }


print ( classe[ 'marius' ]['cuisine'][-1] )

print( json.dumps( classe ) ) 

print( '*' * 45 )

for k, v in classe.items() :
    print( k, v, type( v ) )

    
