liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]

liste = sorted(liste, key=lambda x: x[1], reverse=False)

print(liste)
