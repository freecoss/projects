from Assurable import Assurable
from Maintenable import Maintenable

class Camion(Maintenable, Assurable):
    def __init__(self, immatriculation, date_achat, prix_achat, capacite_charge, etat="disponible"):
        super().__init__(immatriculation, date_achat, prix_achat, etat)
        self.capacite_charge = capacite_charge
    
    def __str__(self):
        return f"{super().__str__()}, Capacité: {self.capacite_charge}"

    def get_capacite_charge(self):
        return self.capacite_charge

    def set_capacite_charge(self, capacite_charge):
        self.capacite_charge = capacite_charge

    def type_vehicule(self):
        return "Camion"
