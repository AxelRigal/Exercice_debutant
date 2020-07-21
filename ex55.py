symbole = "$"
taille = 10
i = 1
for i in range(1, taille + 1):
    nombre = (taille-i)//2
    affiche = [" " for j in range(nombre)] + [(symbole + " ") * i]
    print(*affiche)


for i in range(1, taille + 1):
    espaces = " " * (taille - i)
    print(espaces + (symbole + " ") * i)