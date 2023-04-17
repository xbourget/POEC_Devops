#!/usr/bin/python3
# -*- coding: utf-8 -*-


def typevariable(variable) :
    for i in variable :
        print (i,type(i))
        if type(i)==str : 
            print (i," est une chaine")




tab = [123,"Vincent","3.14",12.56,"Marcel"]

typevariable (tab)