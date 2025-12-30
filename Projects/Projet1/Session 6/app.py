from ex1_suite import CompteBancaire
from gestion_comptes import GestionComptes


def demander_nombre_comptes():
    while True:
        try:
            n = int(input("Saisir le nombre de comptes a ajouter : "))
            if n > 0:
                return n
            print("Le nombre de comptes doit etre strictement positif.")
        except ValueError:
            print("Veuillez saisir un nombre entier valide.")


def main():
    gestion_comptes = GestionComptes()
    n = demander_nombre_comptes()

    for _ in range(n):
        while True:
            try:
                titulaire = input("Saisir le titulaire : ")
                solde = float(input("Saisir le solde : "))
                if not CompteBancaire.verifier_solde(solde):
                    raise ValueError("Le solde doit etre positif.")

                compte = CompteBancaire(titulaire, solde)
                gestion_comptes.ajouter_compte(compte)
                break
            except ValueError as e:
                print(f"Erreur de saisie : {e}. Veuillez recommencer la saisie pour ce compte.")
            except Exception as e:
                print(f"Une erreur est survenue : {e}. Veuillez recommencer la saisie pour ce compte.")

    print("\n" + "=" * 30)
    print("Operations terminees.")
    print(f"Nombre total de comptes crees : {gestion_comptes.nombre_comptes()}")
    print("=" * 30)

    print("\nAffichage de la liste des comptes :")
    gestion_comptes.afficher_comptes()


if __name__ == "__main__":
    main()
        