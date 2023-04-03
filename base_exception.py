#!/usr/bin/python3
# -*- coding: utf-8  -*-


nombre_de_roues = {"tram":18, "voiture": 4, "vélo": 2, "tricycle": 3}


print( 'x' * 10 + 'Exception par error'  )


try :
    del nombre_de_roues[ 'vélo' ] 
except Exception as e:
    print( "la clé n'existe pas")
    print( e )
finally :
    print( "je passe toujours ici")


print( 'x' * 10 + 'raise Exception'  )

try :
    raise Exception( 'mon exception' ) 
except Exception as e:
    print( str(e) )

