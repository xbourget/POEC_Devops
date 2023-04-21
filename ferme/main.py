#!/usr/bin/python3
# -*- coding: utf-8  -*-


from fermeLib.ferme import Ferme
from fermeLib.pature import Pature
from fermeLib.vache import Vache
from fermeLib.cheval import Cheval
from fermeLib.chien import Chien
from fermeLib.mouton import Mouton


ferme = Ferme( 'du moulin' )

ferme.addPature( 'du ruisseau', 3 ) #suface de la pature 3ha

pature = ferme.getPature( 'du ruisseau' )

pature.addElement( Cheval( 'Jumpy Jumper'  ) )
pature.addElement( Chien( 'Rantanplan'  ) )
pature.addElement( Vache( 'marguerite'  ) )
pature.addElement( Vache( 'blanchette'  ) )
pature.addElement( Mouton( 'memeeee'  ) )

ferme.addRessource( 'foin', 300, 'Kg'  )
ferme.addRessource( 'eau',  150, 'litres'  )
ferme.addRessource( 'avoine',  150, 'Kg'  )

ferme.run()
