from Vehicule import Vehicule

class Agence:
    def __init__(self, nom:str, adresse:str):
        self.nom = nom
        self.adresse = adresse
        self.vehicules = []
    
    def ajouterVehicule(self, vehicule_obj):
        if not isinstance(vehicule_obj, Vehicule):
            raise TypeError("L'objet ajouté n'est pas un véhicule")
            
        exist = False
        for v in self.vehicules:
            if v.immatriculation == vehicule_obj.immatriculation:
                exist = True
                break
        
        if not exist:
            self.vehicules.append(vehicule_obj)
        else:
            raise Exception("Ce véhicule existe déjà !")
    
    def rechercheVehicule(self, immatriculation):
        for v in self.vehicules:
            if v.immatriculation == immatriculation:
                return v
        raise Exception("Ce véhicule n'existe pas !")
    
    def inventaire(self):
        if len(self.vehicules) > 0:
            result = []
            for vehicule in self.vehicules:
                result.append(str(vehicule))
            return "\n".join(result)
        else:
            return "Aucun !"
            
    def supprimerVehicule(self, immatriculation):
        veh = self.rechercheVehicule(immatriculation)
        self.vehicules.remove(veh)
    
    def afficher(self):
        print(f"Nom agence : {self.nom} - Adresse : {self.adresse}")
        print("Les véhicules :")
        print(self.inventaire())

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_adresse(self):
        return self.adresse

    def set_adresse(self, adresse):
        self.adresse = adresse

    def get_vehicules(self):
        return self.vehicules

    def set_vehicules(self, vehicules):
        self.vehicules = vehicules
