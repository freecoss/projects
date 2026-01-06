from Agence import Agence
from Voiture import Voiture
from Camion import Camion
from datetime import date

# 1) Création de l'agence
agence = Agence("Agence Auto", "123 Rue Principale")

# 2) Création des véhicules
v1 = Voiture(
    immatriculation="123-A-45", 
    date_achat=date(2022, 5, 10), 
    prix_achat=90000, 
    marque="Toyota", 
    modele="Corolla", 
    couleur="Blanc"
)

v2 = Voiture(
    immatriculation="456-B-78", 
    date_achat=date(2021, 9, 20), 
    prix_achat=120000, 
    marque="Dacia", 
    modele="Duster", 
    couleur="Gris"
)

c1 = Camion(
    immatriculation="789-C-10", 
    date_achat=date(2020, 3, 15), 
    prix_achat=250000, 
    capacite_charge=12.5
)

# 3) Ajout des véhicules à l'agence
agence.ajouterVehicule(v1)
agence.ajouterVehicule(v2)
agence.ajouterVehicule(c1)

print("--- Test Ajout Doublon ---")
try:
    agence.ajouterVehicule(v1)
except Exception as e:
    print(f"Exception levée : {e}")

# 4) Test de la capacité de location pour v1
print("\n--- Test Location v1 ---")
print(f"État initial : {v1}")
v1.louer()
print(f"Après louer() : {v1}")
v1.retourner()
print(f"Après retourner() : {v1}")

try:
    print("Tentative d'un deuxième retour...")
    v1.retourner()
except Exception as e:
    print(f"Exception levée (Retour impossible) : {e}")

# 5) Test de la capacité de maintenance pour le camion
print("\n--- Test Maintenance c1 ---")
print(f"État initial : {c1}")
c1.planifier_maintenance()
print(f"Après planification : {c1}")
c1.effectuer_maintenance()
print(f"Après maintenance : {c1}")

try:
    print("Tentative de maintenance sans planification...")
    c1.effectuer_maintenance()
except Exception as e:
    print(f"Exception levée (Maintenance impossible) : {e}")

# 6) Recherche et suppression
print("\n--- Recherche et Suppression ---")
try:
    res = agence.rechercheVehicule("123-A-45")
    print(f"Véhicule trouvé : {res}")
except Exception as e:
    print(e)

try:
    print("Recherche d'une immatriculation inexistante...")
    agence.rechercheVehicule("000-X-00")
except Exception as e:
    print(f"Exception levée : {e}")

agence.supprimerVehicule("123-A-45")
print("Véhicule 123-A-45 supprimé avec succès.")

# 7) Inventaire final
print("\n--- Inventaire Final ---")
agence.afficher()