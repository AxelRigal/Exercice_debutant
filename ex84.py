def join(*arg):
    separator = arg[0]
    listx = list(arg)
    listx.remove(separator)
    arg = tuple(listx)
    res = ""
    for a in arg:
        if not arg[len(arg)-1] == a :
            res +=  a + separator
        else:
            res += a
    return res
j = join(":", "Bonjour", "tout", "le", "monde")
print(j)
