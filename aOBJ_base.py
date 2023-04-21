#!/usr/bin/python3
# -*- coding: utf-8  -*-

import random 



class Personne:
    # variable static 
    nbrPersonne = 0

    def __init__( self, name, old ):
        self.nom = name
        self.age = old
        self.IDNUM = random.randint( 9000000, 10000000-1   ) 
        Personne.nbrPersonne += 1

    def __str__( self ):
        return "nom : {0} ({1}) ID:{2}".format( self.nom, self.age, self.IDNUM  )

    def __del__( self ):
        #print( 'je detruis ' + self.nom )
        Personne.nbrPersonne -= 1

    def anneeNaissance( self ):
        return 2023 - self.age


class Eleve( Personne ):
    def __init__( self, nom, age, niv ):
        super().__init__( nom, age )
        self.niveau = niv

    def __str__( self ):
        return super().__str__() + ' ' + self.niveau

    def faire( self ):
        print( 'je suis ' + self.nom + ', je suis étudiant en ' + self.niveau )


class Metier( ):
    def __init__( self,  metier ):
        self.metier = metier

    def __str__( self ):
        return self.metier
    
    def retraite( self ):
        return 64 - self.age


class Salarie( Personne, Metier ):
    def __init__( self, nom, age, metier ):
        Personne.__init__( self, nom, age )
        Metier.__init__( self, metier )

    def __str__( self ):
        return super().__str__() + ' ' + self.metier

    def faire( self ):
        print( 'je suis ' + self.nom + ', je suis ' + self.metier )


class Apprenti( Eleve, Metier  ):

    def __init__( self, nom, age, metier, niv ):
        Eleve.__init__( self, nom, age, niv )
        Metier.__init__( self, metier )

    def faire( self ):
        print( self.nom + ', je suis apprenti ' + self.metier + ' de niveau '+ self.niveau   )


def maFonction():
    p1 = Personne( 'Tyty', 19 )
    print( p1 )


if __name__ == '__main__' :

    maFonction()

    p1 = Personne( 'Toto', 19 )
    p2 = Personne( 'Tata', 29 )
    p3 = Personne( 'Titi', 31 )
    p4 = Personne( 'Tutu', 27 )

    print( p1  )
    print( Personne.nbrPersonne )
    print( p1.nbrPersonne )
    del p2
    print( Personne.nbrPersonne )


    e1 = Eleve( 'Nono', 19, "L1")
    print( e1 )

    s1 = Salarie( 'Mumu', 60, 'boulanger'  )

    a1 = Apprenti( 'Jojo', 19, 'plombier', 'BTS')
    listePersonne = []
    listePersonne.append( e1 )
    listePersonne.append( Eleve( 'Nana', 21, "L3")  )
    listePersonne.append( Eleve( 'Nunu', 26, "D")  )
    listePersonne.append( Salarie( 'Momo', 33, 'boucher'  ) )
    listePersonne.append( s1 )
    listePersonne.append( Apprenti( 'Jéjé', 17, 'boulanger', 'CAP'   ) )
    listePersonne.append( Apprenti( 'Juju', 17, 'boulanger', 'CAP'  ) )
    listePersonne.append( a1 )
    listePersonne.append( Salarie( 'Mumu', 27, 'informaticien'  ) )
    listePersonne.append( Salarie( 'Segolène', 27, 'Ambassadeur des Pôles'  ) )

    for p in listePersonne:
        p.faire()

    for p in listePersonne:
        print( p.anneeNaissance() )

    print( s1.retraite(), s1 )
    print( a1.retraite(), a1 )