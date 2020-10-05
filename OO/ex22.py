import random
import string

class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self.numero = numero
        self.balance = balance
        self.virements = {}

    def virement(self, montant):
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits) for i in range(15)))
        self.virements = { result_str : montant }
        self.balance += montant

john = Compte(nom="John Smith", numero="123456", balance=20000)
john.virement(montant=5000)
print(john.balance)
print(john.virements)
