#!/usr/bin/python3
# -*- coding: utf-8  -*-

from My_Ferme import Ferme
from My_Ferme import Cheval 
from My_Ferme import Chien
from My_Ferme import Vache
from My_Ferme import Mouton


ferme = Ferme( 'du moulin' )

ferme.addPature( 'du ruisseau', 3 ) 

pature = ferme.getPature( 'du ruisseau' )

pature.add( Cheval( 'Jumpy Jumper'  ) )
pature.add( Chien( 'Rantanplan'  ) )
pature.add( Vache( 'Milka'  ) )
pature.add( Vache( 'Luska'  ) )
pature.add( Mouton( 'Shawn'  ) )

ferme.addRessource( 'foin', 30, 'tonnes'  )
ferme.addRessource( 'eau',  15000, 'litres'  )
ferme.addRessource( 'avoine',  5, 'tonnes'  )

ferme.run()




