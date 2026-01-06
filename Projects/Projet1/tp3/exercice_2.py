class Personne:
    def __init__(self, nom, prenom, email, tel, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email
        self.__tel = tel
        self.__age = age

    def __str__(self):
        return f"{self.__prenom} {self.__nom} ({self.__age} ans), Email: {self.__email}, Tel: {self.__tel}"

class Adherent(Personne):
    def __init__(self, nom, prenom, email, tel, age, num_adherent):
        super().__init__(nom, prenom, email, tel, age)
        self.num_adherent = num_adherent

    def __str__(self):
        return f"Adhérent N°{self.num_adherent} : " + super().__str__()

class Auteur(Personne):
    def __init__(self, nom, prenom, email, tel, age, num_auteur):
        super().__init__(nom, prenom, email, tel, age)
        self.num_auteur = num_auteur

    def __str__(self):
        return f"Auteur N°{self.num_auteur} : " + super().__str__()

class Livre:
    def __init__(self, isbn, titre, auteur):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return f"Livre: '{self.titre}' (ISBN: {self.isbn})\n   Écrit par: {self.auteur}"

if __name__ == "__main__":
    print("=== Test Exercice 2 ===\n")

    adherent1 = Adherent("Dupont", "Jean", "jean.dupont@email.com", "0601020304", 30, "A001")
    print("--- Adhérent créé ---")
    print(adherent1)
    print("")

    auteur1 = Auteur("Hugo", "Victor", "victor.hugo@academie.fr", "Inconnu", 83, "AUT_VH")
    print("--- Auteur créé ---")
    print(auteur1)
    print("")

    livre1 = Livre("978-0-123456-47-2", "Les Misérables", auteur1)
    print("--- Livre créé ---")
    print(livre1)
