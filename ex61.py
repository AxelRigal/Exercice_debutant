import os

def remonter_dossier(dossier, nombre):
    for i in range(nombre):
         dossier = os.path.dirname(dossier)
    return dossier

dossier = "/Users/Thibh/Desktop/Dossier_01/Tutoriel/Udemy"
print(remonter_dossier(dossier, 0))
