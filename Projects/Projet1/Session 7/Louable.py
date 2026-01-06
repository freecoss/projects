from Vehicule import Vehicule

class Louable(Vehicule):
    def louer(self):
        if self.etat == "disponible":
            self.etat = "loue"
        else:
            raise Exception("Le véhicule n'est pas disponible !")
    
    def retourner(self):
        if self.etat == "loue":
            self.etat = "disponible"
        else:
            raise Exception("Le véhicule n'est pas loué !")
    
    def est_disponible(self):
        return self.etat == "disponible"
