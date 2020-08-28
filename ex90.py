# def replace(phrase, mot_a_remplacer, nouveau_mot):
#     mot = ""
#     phrase_list = list(phrase)
#     for i in range(len(phrase_list)):
#         #print(i)
#         if mot == mot_a_remplacer :
#             for j in range(i, i - len(mot) , -1):
#                 # phrase[j] = mot_a_remplacer[j - i]
#                 print("Phrase " + phrase_list[j])
#                 print("Mot " + mot_a_remplacer[j - i])
#                 print()
#         if phrase_list[i] != " " and phrase_list[i] != "." and phrase_list[i] != ",":
#             mot += phrase_list[i]
#             #print(mot)
#         else:
#             mot = ""
#     print("".join(phrase_list))
#
# phrase = replace("Mon nom est Bond, James Bond.", "Bond", "Tuche")


def replace(phrase, mot_a_remplacer, nouveau_mot):
    while mot_a_remplacer in phrase:
        debut = phrase.index(mot_a_remplacer)
        fin = debut + len(mot_a_remplacer)
        phrase = list(phrase)
        phrase[debut:fin] = list(nouveau_mot)
        phrase = "".join(phrase)
    return phrase

phrase = replace("Mon nom est Bond, James Bond.", "Bond", "Tuche")
print(phrase)
