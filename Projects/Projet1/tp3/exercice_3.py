class Vehicule:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def emettre_son(self):
        print("Le véhicule émet un son inconnu.")

    def afficher_informations(self):
        print(f"Véhicule: {self.nom}, Prix: {self.prix}€")


class Voiture(Vehicule):
    def __init__(self, nom, prix, modele, annee):
        super().__init__(nom, prix)
        self.modele = modele
        self.annee = annee

    def emettre_son(self):
        print("La voiture fait : Vroum Vroum !")

    def afficher_informations(self):
        super().afficher_informations()
        print(f"  Type: Voiture, Modèle: {self.modele}, Année: {self.annee}")


class Moto(Vehicule):
    def __init__(self, nom, prix, marque, puissance):
        super().__init__(nom, prix)
        self.marque = marque
        self.puissance = puissance

    def emettre_son(self):
        print("La moto fait : Vroaaaaap !")

    def afficher_informations(self):
        super().afficher_informations()
        print(f"  Type: Moto, Marque: {self.marque}, Puissance: {self.puissance} ch")


class Avion(Vehicule):
    def __init__(self, nom, prix, compagnie, vitesse_max):
        super().__init__(nom, prix)
        self.compagnie = compagnie
        self.vitesse_max = vitesse_max

    def emettre_son(self):
        print("L'avion fait : Whoooooosh !")

    def afficher_informations(self):
        super().afficher_informations()
        print(f"  Type: Avion, Compagnie: {self.compagnie}, Vitesse Max: {self.vitesse_max} km/h")


if __name__ == "__main__":
    print("=== Test Exercice 3 ===\n")

    v1 = Voiture("Toyota Corolla", 25000, "Corolla Hybride", 2023)
    v2 = Moto("Yamaha MT-07", 7500, "Yamaha", 73)
    v3 = Avion("Airbus A320", 100000000, "Air France", 900)

    vehicules = [v1, v2, v3]

    for v in vehicules:
        v.afficher_informations()
        v.emettre_son()
        print("-" * 30)
