from ex1_suite import CompteBancaire
class GestionComptes:
    def __init__(self):
        self.comptes = []
    
    def ajouter_compte(self,compte:CompteBancaire):
        if not isinstance(compte,CompteBancaire):
            raise ValueError("le compte doit etre une instance de CompteBancaire")
        self.comptes.append(compte)
    
    def afficher_comptes(self):
        if self.comptes:
            for i,compte in enumerate(self.comptes):
                print(f"compte bancaire n^{i+1}")
                compte.afficher()
        else:
            print("Aucun compte a afficher.")
    
    def nombre_comptes(self):
        return len(self.comptes)
    