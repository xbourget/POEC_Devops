#!/usr/bin/python3
# -*- coding: utf-8  -*-

text =  """
fghggngbbfb
 fenfrb
 vrnruifr


 eee

 ee
 e
 e
 e
 e
 th

"""

occurence ={
}

for lettre in text.upper():
    try:
        occurence [lettre]= occurence [lettre] + 1
    except KeyError :
        occurence [lettre] = 1
print(occurence)
