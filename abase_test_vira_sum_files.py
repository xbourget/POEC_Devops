import os

# Chemin du répertoire à analyser
path = "C:/Users/IJF444/source/repos/POEC_Devops"

total_size = 0

for root, directories, files in os.walk(path):
    for filename in files:
        # Chemin complet du fichier
        filepath = os.path.join(root, filename)
        # Taille du fichier
        size = os.path.getsize(filepath)
        # Affichage du nom et de la taille du fichier
        print(f"{filename} ({size} octets)")

        total_size += os.path.getsize(filepath)
print(f"La somme des tailles des fichiers dans le répertoire est {total_size} octets.")