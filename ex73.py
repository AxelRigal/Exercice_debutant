import string
import random

taille = 8
alphabet = string.ascii_lowercase
special_char = string.printable
nombre = list(range(10))
res = list()
for i in range(2):
    res.append(str(alphabet[random.randint(0,25)]))
    res.append(str(alphabet[random.randint(0,25)].upper()))
    res.append(str(nombre[random.randint(0,9)]))
    res.append(str(special_char[random.randint(63, 95)]))
print("".join(res))
