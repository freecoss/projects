Stock=["Ordinateur de bureau", "Ordinateur portable", 100, "Caméra", 310.28, "Hautparleurs", 27.00, "Télévision", 1000, "Cartes mères", "clavier", 500, "barrettes de mémoires"]

print(Stock)

list_chaines = []
liste_nombres = []

for elt in Stock:
    if isinstance(elt,str):
        list_chaines.append(elt)
    else:
        liste_nombres.append(elt)

print(list_chaines)
print(liste_nombres)

print(len(list_chaines))
print(len(liste_nombres))

print(list_chaines.sort())
print(list_chaines.sort(reverse=True))

print(liste_nombres.sort())
print(liste_nombres.sort(reverse=True))