def separateur(p, separator):
    list_sorti = []
    s = ""
    for letter in p:
        if letter == separator:
            list_sorti.append(s)
            s = ""
        else:
            s += letter
    if s:
        list_sorti.append(s)
    return list_sorti
phrase = "bonjour-tout-le-monde"
print(separateur(phrase, "-"))
