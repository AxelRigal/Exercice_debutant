liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
nom_a_chercher = "Julie"
nouveau_nom = "Julien"
liste = [x.replace("Julie", "Julien") for x in liste]
print(liste)