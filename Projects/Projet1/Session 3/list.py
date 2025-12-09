# Définition d'une liste de prénoms
list_prenom = ["ali", "ahmed", "samia"]

# Affiche le nombre d'éléments dans la liste
print(len(list_prenom))

# Remplace l'élément à l'index 1 (deuxième position) par "samia"
list_prenom[1] = "samia"
print(list_prenom)

# Ajoute "salim" à la fin de la liste
list_prenom.append("salim")
print(list_prenom)

# Insère "ahmed" en position 1 (décalera les éléments suivants)
list_prenom.insert(1, "ahmed")

# Nouvelle liste à concaténer
list_prenom1 = ["noura", "souleimane"]

# Étend list_prenom avec les éléments de list_prenom1 (concaténation)
list_prenom.extend(list_prenom1)
print(list_prenom)

# Supprime et renvoie l'élément à l'index 2 (pop prend un index optionnel)
print(list_prenom.pop(2))
print(list_prenom)

# Supprime le dernier élément de la liste (pop sans argument)
list_prenom.pop()

# Supprime la première occurrence de la valeur "noura"
list_prenom.remove("noura")

# Vider la liste (décommenter si nécessaire)
# list_prenom.clear()

# Copie superficielle (shallow copy) : crée une nouvelle liste indépendante des modifications
list_prenom2 = []
list_prenom2 = list_prenom.copy()

# Assignation simple : list_prenom3 référence la même liste (pas une copie).
# Toute modification via list_prenom3 affectera list_prenom.
list_prenom3 = list_prenom

for i in range(len(list_prenom)):
    print(list_prenom[i])
    
for x in list_prenom:
    print(x)

for x,y in enumerate(list_prenom):
    print(x,y)
    
liste = [12,13,14,15,10,20,30]
print(liste[1:5:1])

print(liste[:5])
print(liste[:])
print(liste[::-1])
liste.sort(reverse=True)
print(liste)
