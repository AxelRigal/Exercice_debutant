import os
import string

dossier = os.path.dirname(__file__)
alphabet_dir = os.path.join(dossier, "alphabet")

for letter in string.ascii_uppercase:
    path = os.path.join(alphabet_dir, letter)
    if not os.path.isdir(path):
        # os.makedirs(path)
        print(path)
