nombre = 50
diviseurs = []
for i in range(1, nombre+1):
    if nombre%i == 0 :
        diviseurs.append(i)
print(diviseurs)
