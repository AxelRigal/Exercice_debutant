from datetime import datetime

age = 25
mois_de_naissance = 10
aujourdhui = datetime.today()
if aujourdhui.month < 10 :
    naissance = datetime.today().year - age - 1
else:
    naissance = aujourdhui.year - age
print(naissance)