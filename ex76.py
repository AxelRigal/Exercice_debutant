phrase = "Phrase en camel case"
phrase = phrase[:].lower()
res = []
for mot in phrase.split():
    if mot == "phrase":
        res += mot
    else:
        res += mot.capitalize()


phrase = "Phrase en camel case"
phrase_split = phrase.split()
resultat = [phrase_split.pop(0).lower()]
resultat = resultat + [mot.capitalize() for mot in phrase_split]
resultat_formate = "".join(resultat)

print(resultat_formate)
