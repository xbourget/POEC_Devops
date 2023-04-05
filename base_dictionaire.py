#!/usr/bin/python3
# -*- coding: utf-8  -*-


nombre_de_roues = {"tram":18, "voiture": 4, "vélo": 2, "tricycle": 3}



print( 'x' * 10 + ' for keys'  )

for k in nombre_de_roues.keys():
    print( k, nombre_de_roues[ k ] )


print( 'x' * 10 + ' for values'  )

for i in nombre_de_roues.values():
    print(i)


print( 'x' * 10 + ' for items'  )

for i in nombre_de_roues.items():
    print(i)

del nombre_de_roues[ 'vélo' ] 
nombre_de_roues[ 'monocycle' ] = 1

print( 'x' * 10 + ' for k v'  )

for cle, valeur in nombre_de_roues.items():
        print("l'élément de clé", cle, "vaut", valeur)
