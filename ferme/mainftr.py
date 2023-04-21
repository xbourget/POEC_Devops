#!/usr/bin/python3
# -*- coding: utf-8  -*-

from fermeLib.fermeftr import Ferme
from fermeLib.patureftr import Pature
from fermeLib.vacheftr import Vache



ferme = Ferme( 'du moulin' )

ferme.addPature( 'du ruisseau', 3 ) #suface de la pature 3ha

pature = ferme.getPature( 'du ruisseau' )

pature.addElement( Cheval( 'Jumpy Jumper'  ) )
#pature.addElement( Chien( 'Rantanplan'  ) )
pature.addElement( Vache( 'marguerite'  ) )
pature.addElement( Vache( 'blanchette'  ) )
#pature.addElement( Mouton( 'memeeee'  ) )

ferme.addRessource( 'foin', 30, 'tonnes'  )
ferme.addRessource( 'eau',  15000, 'litres'  )
ferme.addRessource( 'avoine',  5, 'tonnes'  )

ferme.run()




