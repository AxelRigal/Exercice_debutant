employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]
for l in liste:
    if type(l) == str:
        #employes.update({"id-0"+str(len(employes)+1) : l})
        employes["id-{:02d}".format(len(employes)+1)] = l
print(employes)