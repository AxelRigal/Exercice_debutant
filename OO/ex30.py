class Chemin:
    def __init__(self, chemin):
        self.chemin = chemin

    def __str__(self):
        return self.chemin

    def __add__(self, s):
        return Chemin(self.chemin + "/" + s)
c = Chemin("/Users/john")
composite = c + "dossier" + "test" + "script"
print(composite)
