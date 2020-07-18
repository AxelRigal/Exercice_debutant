a = 4
b = 6
c = 2

a1 = min(a, b, c)
a3 = max(a, b, c)
a2 = (a + b + c) - a1 - a3
print("Les nombres dans l'ordre sont {}, {} et {}".format(a1, a2, a3))
