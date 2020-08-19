nombres = []

liste_nombres = range(1000)

for i in liste_nombres:
    if i%7 == 0 and i%3 != 0:
        nombres.append(i)

print(nombres)
