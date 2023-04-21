#!/usr/bin/python3
# -*- coding: utf-8  -*-


from fermeLib.ferme import Ferme
from fermeLib.pature import Pature
from fermeLib.vache import Vache
from fermeLib.cheval import Cheval


ferme = Ferme( 'du moulin' )

ferme.addPature( 'du ruisseau', 3 ) #suface de la pature 3ha

pature = ferme.getPature( 'du ruisseau' )

pature.addElement( Cheval( 'Jumpy Jumper'  ) )
#pature.add( Chien( 'Rantanplan'  ) )
pature.addElement( Vache( 'marguerite'  ) )
pature.addElement( Vache( 'blanchette'  ) )
#pature.add( Mouton( 'memeeee'  ) )

ferme.addRessource( 'foin', 30, 'tonnes'  )
ferme.addRessource( 'eau',  15000, 'litres'  )
ferme.addRessource( 'avoine',  5, 'tonnes'  )

ferme.run()

