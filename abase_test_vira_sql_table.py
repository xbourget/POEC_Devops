import sqlite3

connexion = sqlite3.connect('ma_base_de_donnees.db')

curseur = connexion.cursor()

requete = """CREATE TABLE Employes (
                id INTEGER PRIMARY KEY,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                date_embauche DATE NOT NULL,
                salaire REAL NOT NULL
            )"""

curseur.execute(requete)

connexion.close()
