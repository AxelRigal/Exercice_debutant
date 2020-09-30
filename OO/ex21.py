class Etudiant:
    repertoire = []

    def __init__(self, nom, prenom):
        self.uid = len(self.repertoire) + 1
        self.prenom = prenom
        self.nom = nom
        self.repertoire.append(self)


john = Etudiant("John", "Smith")
julie = Etudiant("Julie", "Martin")
marc = Etudiant("Marc", "Tremblay")
print(Etudiant.repertoire)
print(marc.uid)
