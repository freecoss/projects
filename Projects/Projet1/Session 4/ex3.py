projets = {
"Projet1": {"responsable": "Ali", "budget": 50000, "statut": "en cours"},
"Projet2": {"responsable": "Sara", "budget": 75000, "statut": "terminé"},
"Projet3": {"responsable": "Omar", "budget": 30000, "statut": "en cours"},
"Projet4": {"responsable": "Lina", "budget": 60000, "statut": "en attente"}
}

def projets_en_cours(projets:dict):
    liste = []
    for i,j in projets.items():
        for elt,valeur in j.items():
            if valeur== "en cours":
                liste.append(i)
    return liste
print(projets_en_cours(projets))

def budget_moyen(projets:dict):
    total = 0
    count = 0
    for i,j in projets.items():
        for elt,valeur in j.items():
            if elt == "budget":
                total+=valeur
                count+=1
    return total/count

print(budget_moyen(projets))

def projet_plus_cher(projets):
    max = 0
    nom_projet = ''
    for i,j in projets.items():
        for elt,valeur in j.items():
            if elt == "budget":
                if valeur>max:
                    max = valeur
                    nom_projet = i

    return nom_projet

print(projet_plus_cher(projets))