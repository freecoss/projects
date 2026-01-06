class Paiement:
    def effectuer_paiement(self, montant):
        print(f"Paiement générique de {montant} effectué.")

class CarteCredit(Paiement):
    def __init__(self, numero_carte):
        self.numero_carte = numero_carte

    def effectuer_paiement(self, montant):
        print(f"Paiement de {montant}€ effectué par Carte de Crédit (N° {self.numero_carte})")

class PayPal(Paiement):
    def __init__(self, email):
        self.email = email

    def effectuer_paiement(self, montant):
        print(f"Paiement de {montant}€ effectué via PayPal (Email: {self.email})")

class Commande:
    def __init__(self, montant_commande, moyen_paiement):
        self.montant_commande = montant_commande
        self.moyen_paiement = moyen_paiement # Objet de type Paiement

    def process_payment(self):
        self.moyen_paiement.effectuer_paiement(self.montant_commande)

if __name__ == "__main__":
    print("=== Test Exercice 4 ===\n")

    cb = CarteCredit("1234-5678-9012-3456")
    pp = PayPal("client@example.com")

    cmd1 = Commande(150.00, cb)
    cmd2 = Commande(45.90, pp)
    
    print("--- Traitement Commande 1 ---")
    cmd1.process_payment()
    
    print("\n--- Traitement Commande 2 ---")
    cmd2.process_payment()
