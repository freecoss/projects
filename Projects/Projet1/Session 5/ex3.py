class CompteBancaire:
    nombre_comptes = 0
    def __init__(self,titulaire:str, solde):
        self.__solde = solde
        self.__titulaire = titulaire
        CompteBancaire.nombre_comptes+=1
    

    @property
    def titulaire(self):
        return self.__titulaire
    @titulaire.setter
    def titulaire(self,new_titulaire):
        self.__titulaire = new_titulaire
        
    @property
    def solde(self):
        return self.__solde
    @solde.setter
    def solde(self, new_solde):
        if new_solde >= 0:
            self.__solde = new_solde
        else:
            print("le solde doit etre positive!")
    
    def __str__(self):
        print(f"le titulaire de compte est : {self.__titulaire} avec un solde de : {self.__solde}")
        
    def diposer(self,montant):
        self.__solde+=montant
    def retirer(self, montant):
        if self.__solde>= montant:
            self.__solde-=montant
        else:
            print("montant insifusant!")
        
    @staticmethod
    def verifier_solde(solde):
        if isinstance(solde,(int,float)) and solde>=0:
            return True
        else:
            return False