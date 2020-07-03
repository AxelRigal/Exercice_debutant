chaine = "Pierre, Julien, Anne, Marie, Lucien"
tabChaine = chaine.split(',')
tabChaine = [x.strip(' ') for x in tabChaine]
tabChaine.sort()
separator =(', ')
chaine = separator.join(tabChaine)
print(chaine)
