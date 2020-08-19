import os

cur_dir = os.path.dirname(__file__)
fichier = os.path.join(cur_dir, "fichier.txt")

with open(fichier, "w") as f:
    f.write("Bonjour tout le monde !")
