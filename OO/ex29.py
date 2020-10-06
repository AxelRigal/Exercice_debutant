class Notes:
    tab = []
    def __init__(self):
        self.tab = []

    def ajouter_note(self, note):
        self.tab.append(note)

    def moyenne(self):
        c = 0
        for n in self.tab:
            c += n.valeur
        return round(c/len(self.tab), 1)

    def notes_parfaites(self):
        c = 0
        for n in self.tab:
            if n.valeur == 20:
                c += 1
        return c

class Note:
    def __init__(self, valeur):
        self.valeur = valeur

    def __repr__(self):
        return '{} / 20'.format(self.valeur)

valeur_notes = [12, 19, 14, 13, 9, 20, 8, 15, 4, 20, 19, 17]
notes = Notes()

for valeur_note in valeur_notes:
    notes.ajouter_note(note=Note(valeur=valeur_note))

print(notes.notes_parfaites())
print(notes.moyenne())
