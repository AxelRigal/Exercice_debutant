from glob import glob

dossier = "/Users/thibh/Documents"

fichiers = glob(f"{dossier}/**", recursive=True)
print(len(fichiers))
