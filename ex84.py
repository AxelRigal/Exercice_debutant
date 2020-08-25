def join(*arg):
    separator = arg[0]
    res = ""
    for a in arg[1:]:
        res +=  a + separator
    return res[:-1]
j = join(":", "Bonjour", "tout", "le", "monde")
print(j)

def join(*args):
    resultat = ""

    separateur = args[0]
    elements = args[1:]
    for element in elements:
        resultat += element + separateur

    print(resultat)
    return resultat[:-1]

j = join(":", "Bonjour", "tout", "le", "monde")
print(j)
