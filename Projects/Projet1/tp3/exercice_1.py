class Produit:
    def __init__(self, nom, prix, quantite):
        self.__nom = nom
        self.set_prix(prix)
        self.set_quantite(quantite)

    def get_nom(self):
        return self.__nom

    def get_prix(self):
        return self.__prix

    def get_quantite(self):
        return self.__quantite

    def set_nom(self, nom):
        self.__nom = nom

    def set_prix(self, prix):
        if prix > 0:
            self.__prix = prix
        else:
            print("Erreur : Le prix doit être strictement positif.")
            if not hasattr(self, '_Produit__prix'):
                 self.__prix = 0.0

    def set_quantite(self, quantite):
        if quantite >= 0:
            self.__quantite = int(quantite)
        else:
            print("Erreur : La quantité doit être positive ou nulle.")
            if not hasattr(self, '_Produit__quantite'):
                self.__quantite = 0

    def afficher_infos(self):
        print(f"Produit: {self.__nom}, Prix: {self.__prix}€, Quantité: {self.__quantite}")


class CatalogueProduits:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)
        print(f"Produit '{produit.get_nom()}' ajouté au catalogue.")

    def afficher_tous(self):
        if not self.produits:
            print("Le catalogue est vide.")
        else:
            print("\n--- Catalogue des produits ---")
            for produit in self.produits:
                produit.afficher_infos()
            print("------------------------------\n")

    def valeur_totale_stock(self):
        total = 0
        for produit in self.produits:
            total += produit.get_prix() * produit.get_quantite()
        return total


if __name__ == "__main__":
    print("=== Test Exercice 1 ===\n")
    
    catalogue = CatalogueProduits()

    p1 = Produit("Ordinateur Portable", 999.99, 10)
    p2 = Produit("Souris Sans Fil", 25.50, 50)
    p3 = Produit("Clavier Mécanique", 79.90, 20)
    
    print("Test création produit avec prix négatif :")
    p4 = Produit("Produit Invalide", -10, 5)
    p4.afficher_infos()
    print("")

    catalogue.ajouter_produit(p1)
    catalogue.ajouter_produit(p2)
    catalogue.ajouter_produit(p3)

    catalogue.afficher_tous()

    valeur_totale = catalogue.valeur_totale_stock()
    print(f"Valeur totale du stock : {valeur_totale:.2f}€")