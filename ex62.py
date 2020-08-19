import os
chemin = "/Users/Thibh/Desktop/Dossier_01/../Dossier_02/Udemy"

def normalize_path(chemin):
    chemin_parts = chemin.split("/")
    while ".." in chemin_parts:
        index = chemin_parts.index("..")
        chemin_parts.pop(index)
        chemin_parts.pop(index-1)
    return os.sep.join(chemin_parts)

a = normalize_path(chemin)
print(a)
