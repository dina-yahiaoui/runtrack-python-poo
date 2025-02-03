class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        infos = (
            f"Nom: {self.nom}\n"
            f"Prix HT: {self.prixHT} €\n"
            f"TVA: {self.TVA} %\n"
            f"Prix TTC: {self.calculerPrixTTC():.2f} €"
        )
        return infos

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def get_nom(self):
        return self.nom

    def get_prixHT(self):
        return self.prixHT

    def get_TVA(self):
        return self.TVA


# Création de plusieurs produits
produit1 = Produit("Laptop", 800, 20)
produit2 = Produit("Smartphone", 500, 20)
produit3 = Produit("Tablette", 300, 10)

# Affichage des informations initiales des produits
print("=== Informations initiales ===")
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

# Modification du nom et du prix des produits
produit1.modifier_nom("Laptop Gaming")
produit1.modifier_prix(1000)

produit2.modifier_nom("Smartphone Pro")
produit2.modifier_prix(600)

produit3.modifier_nom("Tablette Lite")
produit3.modifier_prix(250)

# Affichage des nouvelles informations des produits
print("\n=== Informations après modification ===")
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

# Affichage des informations  des produits
print("\n=== Informations individuelles ===")
print(f"Nom du produit 1: {produit1.get_nom()}")
print(f"Prix HT du produit 2: {produit2.get_prixHT()} €")
print(f"TVA du produit 3: {produit3.get_TVA()} %")