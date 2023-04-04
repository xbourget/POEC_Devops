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

def changeName( ficName, ext ):
    fileNameList = ficName.split( '.')
    fileNameList[ :-1 ]
    fileName = ".".join( fileNameList[ :-1 ] ) + "." + ext
    return fileName
    print( ficName.replace("py",ext) )
    #print( ficName.split( '.',-2) )


ext = "bak"
fileName = "/home/work/work/POEC_DEVOPS_Rennes_Mars/POEC_Devops/faireUneFonction.version2.py"
fileName = "/home/work/work/POEC_DEVOPS_Rennes_Mars/POEC_Devops/faireUneFonction.version2.bak"
fileName = changeName( fileName, ext  )
print( fileName )
print( changeName( 'toto.jpg', 'png'  ) )
print( changeName( 'toto.tata.jpg', 'png'  ) )
print( changeName( 'toto.tata.html', 'web'  ) )


#resultat  "/home/work/work/POEC_DEVOPS_Rennes_Mars/POEC_Devops/faireUneFonction.version2.bak"

