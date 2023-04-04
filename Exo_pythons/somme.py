#!/usr/bin/python3
#-*- coding: utf-8 -*-

def somme(list):
    result=0
    for i in list:
        result += i
    return result

print (somme([25, 4, 6 , 84 , 1, 35]))

def moyenne(list):
    result=0
    moyenne=0
    j=0
    for i in list:
        result += i
        j = j + 1
    moyenne = result / j
    return moyenne

print (moyenne([25, 4, 6 , 84 , 1, 35]))

