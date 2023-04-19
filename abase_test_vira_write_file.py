#python3 -m unittest

import unittest


liste = ['carotte', 'tomate', 'broccoli', 'pomme', 'cerise', 'fraise']

nomFichier = 'potager.txt'

file = open ( nomFichier, 'a+' ) #handle

file.writelines ("toto va cherchez des fraises\n")

#file.seek (0)

for ligne in file:
    file.writelines(liste)


print( liste )


text = file.readline()
print( text, end="" )
text = file.readline()
print( text )

file.close()
