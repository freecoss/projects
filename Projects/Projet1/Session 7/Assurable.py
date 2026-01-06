from Vehicule import Vehicule

class Assurable(Vehicule):
    def calculer_montant_assurance(self):
        return self.prix_achat * 0.02
