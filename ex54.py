# Longueur maximale à afficher
n = 8
symbole = '*'
compte = 1
while compte < n:
    print(symbole * (compte))
    compte += 1
while compte > 0:
    print(symbole * (compte))
    compte -= 1

nombres = list(range(1, n+1)) + list(range(n-1, 0, -1))
for i in nombres:
    print(symbole*i)