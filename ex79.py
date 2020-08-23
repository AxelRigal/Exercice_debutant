import string

phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"
phrase = phrase.lower()
alphabet = list(string.ascii_lowercase)
for letter in phrase:
    if letter in alphabet:
        alphabet.remove(letter)
if alphabet:
    print("La phrase n'est pas un Pangramme")
else:
    print("La phrase est un Pangramme")
