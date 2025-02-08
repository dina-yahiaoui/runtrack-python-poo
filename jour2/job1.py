class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # Attribut privé
        self.__largeur = largeur    # Attribut privé

    # Accesseurs (getters)
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setters)
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

# Création d'un rectangle avec longueur 10 et largeur 5
rect = Rectangle(10, 5)

# Affichage des valeurs initiales
print("Longueur initiale :", rect.get_longueur())
print("Largeur initiale :", rect.get_largeur())

# Modification des valeurs
rect.set_longueur(15)
rect.set_largeur(7)

# Vérification des modifications
print("Nouvelle longueur :", rect.get_longueur())
print("Nouvelle largeur :", rect.get_largeur())
