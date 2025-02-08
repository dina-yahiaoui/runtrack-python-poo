# Classe Rectangle
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

    # Méthode pour calculer le périmètre
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    # Méthode pour calculer la surface
    def surface(self):
        return self.__longueur * self.__largeur

# Classe Parallelepipede héritant de Rectangle
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)  # Appel au constructeur de la classe parente
        self.__hauteur = hauteur            # Attribut privé

    # Accesseur pour la hauteur
    def get_hauteur(self):
        return self.__hauteur

    # Mutateur pour la hauteur
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    # Méthode pour calculer le volume
    def volume(self):
        return self.surface() * self.__hauteur

# Instanciation de la classe Rectangle
rect = Rectangle(5, 3)

# Vérification du périmètre et de la surface
print(f"Périmètre du rectangle: {rect.perimetre()}")  # Périmètre = 2 * (5 + 3) = 16
print(f"Surface du rectangle: {rect.surface()}")      # Surface = 5 * 3 = 15

# Instanciation de la classe Parallelepipede
parallelepipede = Parallelepipede(5, 3, 10)

# Vérification du volume
print(f"Volume du parallélépipède: {parallelepipede.volume()}")  # Volume = surface * hauteur = 15 * 10 = 150
