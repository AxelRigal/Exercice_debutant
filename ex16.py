lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
compter = 0
for lettre in phrase:
    if lettre == lettre_a_chercher:
        compter += 1
print(str(compter))
