import os
from glob import glob

dossier = "/home/axel/workspace/Exercice_debutant"
mot = "Python"

fichiers = glob(f"{dossier}/**/*.txt", recursive=True)

fichiersTrouve = []

for filename in fichiers:
    with open(filename, "r") as file:
        contenu_fichier = file.read()
        if mot in contenu_fichier:
            fichiersTrouve.append(filename)
print(fichiersTrouve)
