class CustomeListe(object):
    def __init__(self, *args):
        self.valeurs = []
        for arg in args:
            if arg not in self.valeurs and not arg.isdigit():
                self.valeurs.append(arg)
    def append(self, mot):
        if type(mot) != int:
            if not mot.isnumeric() and mot not in self.valeurs:
                self.valeurs.append(mot)
                
ma_liste = CustomeListe("Pierre", "Julien", "Marie")
ma_liste.append(5)
ma_liste.append("Pierre")
print(ma_liste.valeurs)
