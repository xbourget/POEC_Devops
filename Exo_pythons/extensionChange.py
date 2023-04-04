#!/usr/bin/python3
# -*- coding: utf-8  -*-

#ext="bak"
#fileName = "/home.py"
def changeName( fileName, ext):
    fileNameList= fileName.split( '.' )
    fileNameList[ :-1 ]
    fileName=".".join( fileNameList[:-1]) + "." + ext
    return fileName


print (changeName("titi.py", "png"))