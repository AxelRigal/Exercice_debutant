import random

mot = "Bonjour"
mot2 = []
used = []
while len(mot2) < len(mot):
    r = random.randint(0, len(mot)-1)
    if r not in used:
        mot2.append(mot[r])
        used.append(r)
print("".join(mot2).capitalize())
