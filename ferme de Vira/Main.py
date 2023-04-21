#!/usr/bin/python3
# -*- coding: utf-8  -*-


from myfermeLib.ferme import Ferme
from myfermeLib.pature import Pature
from myfermeLib.vache import Vache
from myfermeLib.cheval import Cheval


ferme = Ferme( 'du moulin' )

ferme.addPature( 'du ruisseau', 3 ) #suface de la pature 3ha

pature = ferme.getPature( 'du ruisseau' )

pature.addElement( Cheval( 'Jumpy Jumper'  ) )
#pature.add( Chien( 'Rantanplan'  ) )
pature.addElement( Vache( 'Milka'  ) )
pature.addElement( Vache( 'Luska'  ) )
#pature.add( Mouton( 'memeeee'  ) )

ferme.addRessource( 'foin', 30, 'tonnes'  )
ferme.addRessource( 'eau',  15000, 'litres'  )
ferme.addRessource( 'avoine',  5, 'tonnes'  )

ferme.run()
