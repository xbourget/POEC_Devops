#!/usr/bin/python3
# -*- coding: utf-8  -*-

def evalOperateur ( toEval ) :
    print( "{0} = {1}".format( toEval, eval(toEval)) )


evalOperateur( "5 + 3" )
evalOperateur( "5 - 3")
evalOperateur( "- 3")
evalOperateur( "5 * 3")
evalOperateur( "12 / 3")
evalOperateur( "5 % 2")
evalOperateur( "5 ** 2")
evalOperateur( "15 // 2")


print('x' * 10 + ' or logique'  )
evalOperateur( "5 and 3")
evalOperateur( "5 and 0")
evalOperateur( "5 and 0 and 6")
evalOperateur( "True and False" )
evalOperateuror "True and True" )

print('x' * 10 + ' and binaire'  )
evalOperateur( "5 & 3")
evalOperateur( "True & 3" )
evalOperateur( "True & 0" )
evalOperateur( "True & True" )

print( 'x' * 10 + ' or logique'  )
evalOperateur( "0  or 3 or 5")
evalOperateur( "True or False" )
evalOperateur( "True or True" )

print( 'x' * 10 + ' or binaire'  )
evalOperateur( "5 | 3")
evalOperateur( "True | False" )
evalOperateur( "True | True" )

print( 'x' * 10 + ' complément'  )
evalOperateur( "0b00000000000000000000000000000011" )
evalOperateur( "-0b00000000000000000000000000000011" )
evalOperateur( "~0b00000000000000000000000000000011" )
evalOperateur( "~True" )
evalOperateur( "-True" )

print( 'x' * 10 + ' décalage'  )
evalOperateur( "1 > 2" )
evalOperateur( "8 < 1" )
