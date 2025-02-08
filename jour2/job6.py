from abc import ABC, abstractmethod

class Commande(ABC):
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire des plats : {nom: (prix, quantité)}
        self.__statut = "en cours"

    def ajouter_plat(self, nom, prix, quantite=1):
        if self.__statut != "en cours":
            print("Impossible d'ajouter un plat à une commande terminée ou annulée.")
            return
        if nom in self.__plats_commandes:
            self.__plats_commandes[nom] = (prix, self.__plats_commandes[nom][1] + quantite)
        else:
            self.__plats_commandes[nom] = (prix, quantite)
        print(f"Plat {nom} ajouté ({quantite}x, {prix}€ chacun).")

    def annuler_commande(self):
        if self.__statut == "en cours":
            self.__statut = "annulée"
            self.__plats_commandes.clear()
            print("Commande annulée.")
        else:
            print("La commande ne peut pas être annulée.")

    def terminer_commande(self):
        if self.__statut == "en cours":
            self.__statut = "terminée"
            print("Commande terminée.")
        else:
            print("La commande est déjà terminée ou annulée.")

    def __calculer_total(self):
        return sum(prix * quantite for prix, quantite in self.__plats_commandes.values())

    def afficher_commande(self):
        print(f"Commande #{self.__numero_commande} - Statut: {self.__statut}")
        for nom, (prix, quantite) in self.__plats_commandes.items():
            print(f"  - {nom} x{quantite} : {prix * quantite}€")
        total = self.__calculer_total()
        print(f"Total à payer: {total}€ (TVA incluse: {self.calculer_tva()}€)")

    def calculer_tva(self, taux_tva=0.2):
        return round(self.__calculer_total() * taux_tva, 2)

# Test de la classe Commande
commande = Commande(1)
commande.ajouter_plat("Pizza", 12, 2)
commande.ajouter_plat("Pâtes", 10, 1)
commande.afficher_commande()
commande.terminer_commande()
commande.ajouter_plat("Salade", 6)
commande.afficher_commande()
commande.annuler_commande()
