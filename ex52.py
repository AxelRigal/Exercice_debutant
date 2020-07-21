import string
alphabet = string.ascii_lowercase
dictAlphabet = {}
for lettre in range(len(alphabet)):
    dictAlphabet[lettre+1] = alphabet[lettre]

print(dictAlphabet)

indices = range(1, len(alphabet) + 1)
liste_zip = zip(indices, alphabet)
resultat = dict(liste_zip)

print(resultat)