class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde=0.0, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte N°{self.__numero_compte}\nTitulaire: {self.__prenom} {self.__nom}\nSolde: {self.__solde:.2f}€\nDécouvert autorisé: {'Oui' if self.__decouvert else 'Non'}")

    def afficherSolde(self):
        print(f"Solde actuel: {self.__solde:.2f}€")

    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant:.2f}€ effectué. Nouveau solde: {self.__solde:.2f}€")
        else:
            print("Le montant du versement doit être positif.")

    def retrait(self, montant):
        if montant > 0:
            if self.__solde - montant >= 0 or self.__decouvert:
                self.__solde -= montant
                print(f"Retrait de {montant:.2f}€ effectué. Nouveau solde: {self.__solde:.2f}€")
            else:
                print("Fonds insuffisants pour ce retrait.")
        else:
            print("Le montant du retrait doit être positif.")

    def agios(self):
        if self.__solde < 0:
            frais = abs(self.__solde) * 0.05  # Exemple : 5% d'agios sur le montant négatif
            self.__solde -= frais
            print(f"Des agios de {frais:.2f}€ ont été appliqués. Nouveau solde: {self.__solde:.2f}€")

    def virement(self, compte_destinataire, montant):
        if montant > 0:
            if self.__solde - montant >= 0 or self.__decouvert:
                self.__solde -= montant
                compte_destinataire.versement(montant)
                print(f"Virement de {montant:.2f}€ effectué vers le compte N°{compte_destinataire.__numero_compte}.")
            else:
                print("Fonds insuffisants pour effectuer le virement.")
        else:
            print("Le montant du virement doit être positif.")

# Création des comptes
titulaire1 = CompteBancaire("123456", "Doe", "John", 1000.0)
titulaire2 = CompteBancaire("654321", "Smith", "Alice", -200.0, decouvert=True)

# Vérification des fonctionnalités
titulaire1.afficher()
titulaire2.afficher()
titulaire1.versement(500)
titulaire1.retrait(300)
titulaire1.afficherSolde()
titulaire2.agios()
titulaire1.virement(titulaire2, 200)
titulaire2.afficherSolde()
