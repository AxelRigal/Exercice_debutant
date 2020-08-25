def recuperer_item(list, index):
    try:
        return list[index]
    except IndexError:
        return "Index {0} hors de la liste".format(index)

list = ["Julien", "Marie", "Pierre"]

print(recuperer_item(list, 0))
print(recuperer_item(list, 5))
print(recuperer_item(list, -13))
