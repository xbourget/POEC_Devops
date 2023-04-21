#!/usr/bin/python3
# -*- coding: utf-8  -*-




ferme = Ferme( 'du moulin' )

ferme.addPature( 'du ruisseau', 3 ) #suface de la pature 3ha

pature = ferme.getPature( 'du ruisseau' )

pature.add( Cheval( 'Jumpy Jumper'  ) )
pature.add( Chien( 'Rantanplan'  ) )
pature.add( Vache( 'marguerite'  ) )
pature.add( Vache( 'blanchette'  ) )
pature.add( Mouton( 'memeeee'  ) )

ferme.addRessource( 'foin', 30, 'tonnes'  )
ferme.addRessource( 'eau',  15000, 'litres'  )
ferme.addRessource( 'avoine',  5, 'tonnes'  )

ferme.run()



