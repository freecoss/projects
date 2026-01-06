from Vehicule import Vehicule

class Maintenable(Vehicule):
    def planifier_maintenance(self):
        if self.etat != "maintenance":
            self.etat = "maintenance"
    
    def effectuer_maintenance(self):
        if self.etat == "maintenance":
            self.etat = "disponible"
        else:
            raise Exception("Le véhicule n'est pas en maintenance !")