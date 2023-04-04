#!/usr/bin/python3
# -*- coding: utf-8  -*-
1
2
3
4
5
6
import os



print()
print()


chaine = "il fait, beau, mais un peu frais"
print( chaine )


lesMots = chaine.split( ' ' )
print( lesMots )

lesMots = chaine.split( ',' )
print( lesMots )

maChaine = "XXXXX".join( lesMots )
print( maChaine )

maChaine = ",".join( lesMots )
print( maChaine )

print()
print( '*' * 50 )
print()

fileName = "/home/work/work/POEC_DEVOPS_Rennes_Mars/POEC_Devops/faireUneFonction.version2.py"
fileName = "/home/work/work/POEC_DEVOPS_Rennes_Mars/POEC_Devops/faireUneFonction.version2.html"

fileNameList = fileName.split( '.')

print( fileNameList[ -1] )
print( fileNameList[ 0 ] + ".copy" )

fileNameList = fileName.split( '/')

print( fileNameList[ -1] )

def changeName( ficName, ext )

ext = "bak"
fileName = "/home/work/work/POEC_DEVOPS_Rennes_Mars/POEC_Devops/faireUneFonction.version2.py"
for file in fileName:
    file.replace(".py",".ext")
fileName = changeName( fileName, ext  )

#resultat  "/home/work/work/POEC_DEVOPS_Rennes_Mars/POEC_Devops/faireUneFonction.version2.bak"

    