class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def position(self):
        return (self.x, self.y)

    def droite(self):
        self.x += 1

    def bas(self):
        self.y += 1

    def gauche(self):
        self.x -= 1

    def haut(self):
        self.y -= 1


perso = Personnage(2, 3)

print("Position initiale:", perso.position())  # Sortie: (2, 3)

perso.droite()
print("Après déplacement à droite:", perso.position())  # Sortie: (3, 3)

perso.bas()
print("Après déplacement en bas:", perso.position())  # Sortie: (3, 4)

perso.gauche()
print("Après déplacement à gauche:", perso.position())  # Sortie: (2, 4)

perso.haut()
print("Après déplacement en haut:", perso.position())  