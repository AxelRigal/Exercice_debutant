class Voiture:
    def __init__(self, marque, prix):
        self.marque = marque
        self.prix = prix

    def changer_prix(self, prix):
        if isinstance(prix, int):
            self.prix = prix
