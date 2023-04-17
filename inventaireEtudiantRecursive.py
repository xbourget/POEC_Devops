#!/usr/bin/python3
# -*- coding: utf-8  -*-

#  [ ]

import os
import json
import sys

from os.path import isfile, join


print( 'wwww', sys.argv[0] )

if len(sys.argv) < 2 :
    print( '    usage : inventaireEtudiantRecursive.py  path')
    exit( 0 )

repertoireBaseName = sys.argv[1]

liste = []


def explorePath( path, tab=''  ):            
    for entry in os.listdir( path ): 
        pathLocal  = path + '/' + entry
        #print( tab, entry , type(entry) )
        if not isfile( pathLocal ) :
            print( 'tab', pathLocal, 'repertory')

            etudiant = pathLocal.split( '/' )[-1] 
            liste.append( etudiant )            
            explorePath( pathLocal , tab  + '    '     )
            

explorePath(  repertoireBaseName )





print( liste )

file  = open( 'result.txt', 'w') 
for etudiant in liste:
    file.writelines( etudiant + "\n" )
file.close()



