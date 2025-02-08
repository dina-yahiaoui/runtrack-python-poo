# Classe Forme avec la méthode aire
class Forme:
    def aire(self):
        return 0

# Classe Rectangle héritant de Forme
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    # Surcharge de la méthode aire
    def aire(self):
        return self.largeur * self.hauteur

# Création d'un rectangle
rect = Rectangle(5, 3)

# Affichage de l'aire du rectangle
print(f"L'aire du rectangle est : {rect.aire()}")  # Résultat : L'aire du rectangle est : 15
