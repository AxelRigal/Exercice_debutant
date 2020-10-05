class Personnage:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom


class Magicien(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.puissance = 80


class Gobelin(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.puissance = 20


class Chevalier(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom, nom)
        self.puissance = 70


c = Chevalier("chevalier1", "chevalier")
m = Magicien("magicien1", "mage")
g = Gobelin("gobelin1", "gob")

print(" %s  ,  %s  , %s" % (c.nom, c.prenom, c.puissance))
print(" %s  ,  %s  , %s" % (m.nom, m.prenom, m.puissance))
print(" %s  ,  %s  , %s" % (g.nom, g.prenom, g.puissance))
