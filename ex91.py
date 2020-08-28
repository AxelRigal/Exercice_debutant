class SuperChaine(object):
    def __init__(self, chaine):
        self.chaine = chaine

    def majuscule(self):
        return str(self.chaine).upper()
    def minuscule(self):
        return str(self.chaine).lower()
    def titre(self):
        return str(self.chaine).capitalize()

chaine = SuperChaine("UdeMy")
print(chaine.majuscule())
print(chaine.minuscule())
print(chaine.titre())
