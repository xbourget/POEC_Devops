#!/usr/bin/python3
# -*- coding: utf-8  -*-

from random import randint 
from json import dump, dumps 

#int tableau[10][10];


dico = { "pierre" : 41, "julie" : 27, "Gontrand" : 41 }

print(  dico )

print(  list(dico.keys()) )
print(  dico.values() )
print(  dico.items() )


dico[ 'toto' ] = 15
del dico[ 'pierre' ]

dico[ 12 ] = 'chat'



for k in dico.keys():
    print( k, '->', dico[ k ] )


for k, v in dico.items():
    print( k, '=>', v )


classe = {}

classe[ 'toto' ] = { 'age' : 13, 'moyenne' : 16, 'sport' : { 'hiver' : 'hockey', 'ete': ['natation', 'voile', 'pétanque']  }  }
classe[ 'tata' ] = { 'moyenne' : 18, 'musique' : { 'moderne' : 'pink floyd', 'classique': ['mozart', 'chopin', 'schuber']  }  }


print( classe['toto']['moyenne']  )
print( classe['toto']['sport']  )
print( classe['toto']['sport']['ete'][1]  )
print( classe['toto']['sport']['ete']  )
print( classe )
print( 'XXX', dumps( classe) )

print( classe['tata']['sport']  )










