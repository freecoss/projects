class CompteBancaire:
    def __init__(self,titulaire:str, solde):
        if solde >= 0:
            self.__solde = solde
        else:
            self.__solde = 0
        self.__titulaire = titulaire
    

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
        
