from abc import ABC, abstractmethod
from datetime import date

class Vehicule(ABC):
    def __init__(self, immatriculation: str, date_achat: date, prix_achat: int, etat: str = "disponible"):
        self.immatriculation = immatriculation
        self.date_achat = date_achat
        
        if etat in ["disponible", "loue", "maintenance"]:
            self.etat = etat
        else:
            raise ValueError("L'etat doit etre soit disponible, loue ou maintenance !")
        self.prix_achat = prix_achat
        
    def get_immatriculation(self):
        return self.immatriculation

    def set_immatriculation(self, immatriculation):
        self.immatriculation = immatriculation

    def get_date_achat(self):
        return self.date_achat

    def set_date_achat(self, date_achat):
        self.date_achat = date_achat

    def get_etat(self):
        return self.etat

    def set_etat(self, etat):
        if etat in ["disponible", "loue", "maintenance"]:
            self.etat = etat
        else:
            raise ValueError("L'etat doit etre soit disponible, loue ou maintenance !")

    def get_prix_achat(self):
        return self.prix_achat

    def set_prix_achat(self, prix_achat):
        self.prix_achat = prix_achat

    def __str__(self):
        return f"Matricule: {self.immatriculation}, Date achat: {self.date_achat}, Etat: {self.etat}, Prix: {self.prix_achat}"
    
    @abstractmethod
    def type_vehicule(self):
        pass
