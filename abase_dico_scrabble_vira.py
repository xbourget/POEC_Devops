from unidecode import unidecode

points = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 10, 'L': 1, 'M': 2, 'N': 1, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10}

text = """
Si vous donnez aux histoires que vous écrivez à la première personne une vraisemblance telle que 
les gens finissent par y croire, le lecteur pensera presque forcément qu'elles vous sont effectivement arrivées. Ce qui est tout à fait nature lpuisqu', au moment où vous les inventez , il faut bien que vous donniez l'impression qu'elles sont arrivées à celui qui les raconte. Si votre entreprise est réussie, vous amenez celui qui les lit à croire que ces choses là lui sont également arrivées à lui. Le but que vous vous êtes assigné est atteint, 
ou peu s'en faut : créer quelque chose susceptible d'imprégner l'expérience et la mémoire de votre lecteur.
"""

text_without_accent = unidecode(text)

mots = text_without_accent.split()

sommes_points = []
for mot in mots:
    points_mot = sum(points.get(lettre.upper(), 0) for lettre in mot)
    sommes_points.append(points_mot)

for i in range(len(mots)):
    print(f"{mots[i]}: {sommes_points[i]} points")

somme_totale = sum(sommes_points)
print(f"La somme totale des points pour le texte est : {somme_totale} points.")
