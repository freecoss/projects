from Assurable import Assurable
from Louable import Louable
from Maintenable import Maintenable

class Voiture(Louable, Assurable, Maintenable):
    def __init__(self, immatriculation, date_achat, prix_achat, marque, modele, couleur, etat="disponible"):
        super().__init__(immatriculation, date_achat, prix_achat, etat)
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
    
    def __str__(self):
        return f"{super().__str__()}, Marque: {self.marque}, Modele: {self.modele}, Couleur: {self.couleur}"

    def get_marque(self):
        return self.marque

    def set_marque(self, marque):
        self.marque = marque

    def get_modele(self):
        return self.modele

    def set_modele(self, modele):
        self.modele = modele

    def get_couleur(self):
        return self.couleur

    def set_couleur(self, couleur):
        self.couleur = couleur

    def type_vehicule(self):
        return "Voiture"
