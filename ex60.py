import string

employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]

alphabet = string.ascii_lowercase
milieu = int(len(alphabet) / 2)
alphabet_01, alphabet_02 = alphabet[:milieu], alphabet[milieu:]

employes_a_m = []
employes_n_z = []

for employe in employes:
    premiere_lettre = employe[0].lower()
    if premiere_lettre in alphabet_01:
        employes_a_m.append(employe)
    elif premiere_lettre in alphabet_02:
        employes_n_z.append(employe)

print("Employés de A à M:", ", ".join(sorted(employes_a_m)))
print("Employés de N à Z:", ", ".join(sorted(employes_n_z)))

employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]

alphabet = string.ascii_lowercase
employes_a_m = [e for e in employes if e[0].lower() in alphabet[:13]]
employes_n_z = [e for e in employes if e[0].lower() in alphabet[13:]]

print("Employés de A à M:", ", ".join(sorted(employes_a_m)))
print("Employés de N à Z:", ", ".join(sorted(employes_n_z)))
