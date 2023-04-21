#!/usr/bin/python3
# -*- coding: utf-8  -*-


from geoLib.point import Point
from geoLib.plan import Plan
from geoLib.carre import Carre
from geoLib.cercle import Cercle
from geoLib.rectangle import Rectangle


p1 = Point( 4, -6 )
p2 = Point( 40, 6 )

print( Point.nbrPoint )

plan  = Plan()

#r1.surface()

plan.addElement( Carre( 10, 45, 60  ) )
plan.addElement( Cercle( 101, -185, 10  ) )
plan.addElement( Point( 0, 0  ) )
#plan.addElement( Rectangle( 7, 20, 8, 45  ) )

print( plan.surface() )

r1 = Rectangle( 7, 20, 1, 5  )
r2 = Rectangle( 7, 20, 10, 10  )
print( r1.calculeSurface( 10, 50) )

print( '>>',r1 + r2)



print( Rectangle.calculeSurface( 10, 50) )

print( Cercle.PI )

print( r2 )

print( r2.__dict__ )
print( r2.__dict__.keys() )
print( hash(r2) )

