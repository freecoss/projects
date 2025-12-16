def multiple_params(*args):
    for elmt in args:
        print(elmt)

# Passage d'argument par valeur (les entiers sont immuables)
def add_cinq(a: int):
    a += 5
    return a
    
def modifie_list(liste: list):
    liste.append(6)

# Appel de multiple_params avec plusieurs arguments
multiple_params(3, 4, 5, 7)

# Appel de add_cinq
x = int(input("Saisir un nombre : "))
resultat = add_cinq(x)
print(f"Nombre original : {x}, après add_cinq : {resultat}")

# Test de modifie_list
ma_liste = [1, 2, 3, 4, 5]
print(f"Liste avant : {ma_liste}")
modifie_list(ma_liste)
print(f"Liste après : {ma_liste}")