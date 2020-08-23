def isdigit(variable):
    for i in variable:
        if i not in [str(n) for n in range(10)]:
            return False
    return True
print(isdigit("1854274"))
