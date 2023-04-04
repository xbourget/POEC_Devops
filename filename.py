#!/usr/bin/python3
# -*- coding: utf-8  -*-

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


def changeName( fileName, ext ):
    fileNameList = fileName.split( '.')
    fileNameList [ :-1 ]
    fileName = "." .join (fileNameList[ :-1 ]) + "." + ext
    return(fileName)
ext = "bak"
fileName = "/home/work/work/POEC_DEVOPS_Rennes_Mars/POEC_Devops/faireUneFonction.version2.py"
fileName = changeName( fileName, ext )

    


#resultat  "/home/work/work/POEC_DEVOPS_Rennes_Mars/POEC_Devops/faireUneFonction.version2.bak"

