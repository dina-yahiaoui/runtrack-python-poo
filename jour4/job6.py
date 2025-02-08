# Classe Vehicule
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Prix: {self.prix}€")

    def demarrer(self):
        print("Attention, je roule")

# Classe Voiture qui hérite de Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule()  # Appel de la méthode de la classe parente
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("La voiture démarre, vroom vroom!")

# Classe Moto qui hérite de Vehicule
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue

    def informationsVehicule(self):
        super().informationsVehicule()  # Appel de la méthode de la classe parente
        print(f"Nombre de roues: {self.roue}")

    def demarrer(self):
        print("La moto démarre, brrrrrm!")

# Instanciation d'un objet Voiture
voiture = Voiture("Toyota", "Corolla", 2020, 20000)
voiture.informationsVehicule()
voiture.demarrer()

# Instanciation d'un objet Moto
moto = Moto("Yamaha", "MT-07", 2021, 8000)
moto.informationsVehicule()
moto.demarrer()

