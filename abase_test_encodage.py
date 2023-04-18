#!/usr/bin/python3
# -*- coding: utf-8  -*-

import unicodedata


"""
2167    'Ⅷ'; ROMAN NUMERAL EIGHT
2168    'Ⅸ'; ROMAN NUMERAL NINE
...
265E    '♞'; BLACK CHESS KNIGHT
265F    '♟'; BLACK CHESS PAWN
...
1F600   '😀'; GRINNING FACE
1F609   '😉'; WINKING FACE
"""


u = chr(0X2168) + 'abcdéàÉÀ' + chr(0X265E) + chr(0X1F600) 
u = 'abcdéàÉÀ'
print('ori', u )
#print('ori', u.decode( 'ascii' ) )
print( 'utf', u.encode('utf-8').decode() )
#print( u.encode('ascii') ) 
print( 'ignore',u.encode('ascii', 'ignore').decode() )
print( 'replace',u.encode('ascii', 'replace').decode() )
print( 'xml', u.encode('ascii', 'xmlcharrefreplace').decode() )
print( 'backslash',u.encode('ascii', 'backslashreplace').decode() )
print( 'name replace',u.encode('ascii', 'namereplace').decode())

print( 'w' * 50 )


def strip_accents(text):
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)
 

print( strip_accents( u ) )



