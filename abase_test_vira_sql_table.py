import sqlite3

connexion = sqlite3.connect('ma_base_de_donnees.db')
curseur = connexion.cursor()

# Inserting data
curseur.execute("INSERT INTO Employes (id, nom, prenom, date_embauche, salaire) VALUES (1, 'Doe', 'John', '2022-01-01', 5000.00)")
curseur.execute("INSERT INTO Employes (id, nom, prenom, date_embauche, salaire) VALUES (2, 'Smith', 'Jane', '2022-01-01', 6000.00)")

connexion.commit()

# Read data
conn = sqlite3.connect('ma_base_de_donnees.db')

cursor = conn.cursor()

cursor.execute("SELECT id, name FROM Employees")

rows = cursor.fetchall()

for row in rows:
    print(row)

connexion.close()

