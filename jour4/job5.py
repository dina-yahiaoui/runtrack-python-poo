import math

# Classe Forme de base
class Forme:
    def aire(self):
        pass

# Classe Rectangle qui hérite de Forme
class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self):
        return self.longueur * self.largeur

# Classe Cercle qui hérite de Forme
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    
    # Surcharge de la méthode aire pour un cercle
    def aire(self):
        return math.pi * (self.radius ** 2)

# Test des différentes classes

# Création d'une instance Rectangle
rectangle = Rectangle(5, 3)
print(f"Aire du rectangle : {rectangle.aire()}")

# Création d'une instance Cercle
cercle = Cercle(4)
print(f"Aire du cercle : {cercle.aire()}")
