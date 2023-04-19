from myLib.scrabble import scrabble

nomFichier = 'monDico.txt'
file = open(nomFichier, 'w') # handle

for letter in scrabble.keys():
    point = scrabble[letter]["point"]
    nombre = scrabble[letter]["nombre"]
    print("Letter {letter:<3s} -> {point:<2d} points ({nombre:<2d} occurences)".format(letter=letter, point=point, nombre=nombre))
    file.write("Letter {letter:<3s} -> {point:<2d} points ({nombre:<2d} occurences)\n".format(letter=letter, point=point, nombre=nombre))

file.close()

