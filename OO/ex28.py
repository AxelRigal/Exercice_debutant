import string
import random

class PasswordGenerator:

    @classmethod
    def generate(cls, longueur):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join((random.choice(letters_and_digits) for i in range(longueur)))


mot_de_passe = PasswordGenerator.generate(15)
print(mot_de_passe)
