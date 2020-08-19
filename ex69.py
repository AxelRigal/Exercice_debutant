import os
import time

dossier =  "/test/1"
dossier_a_chercher = "Test"

attente = input("Entrez un temps de raffraichissement")
while dossier_a_chercher not in os.listdir(dossier):
    print("dossier introuvable")
    time.sleep(int(attente))

print("Trouvé")
