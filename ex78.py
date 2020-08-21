mot = "Un roc cornu"
mot = mot.lower()
mot = mot.replace(" ", "")
moitier = int(len(mot)/2)
list_mot = []
res = ""
res2 = ""
for i in range(moitier):
    res += mot[i]
for j  in range(int(len(mot)/2)):
    list_mot.append(mot[j + int(len(mot)/2) ])
for k in list_mot[::-1]:
    res2 += str(k)
if res == res2:
    print(True)


mot = "Un roc cornu"
 
mot_lower = mot.lower().replace(" ", "")

if mot_lower == mot_lower[::-1]:
    print(True)
else:
    print(False)
