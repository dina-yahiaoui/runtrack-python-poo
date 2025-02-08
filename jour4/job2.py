# Classe Personne
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")

# Classe Eleve héritée de Personne
class Eleve(Personne):
    def __init__(self, nom, age):
        super().__init__(nom, age)

    def allerEnCours(self):
        print("Je vais en cours.")

    def bonjour(self):
        super().bonjour()  # Appel à la méthode bonjour de la classe Personne
        print("Je suis un élève.")

# Classe Professeur héritée de Personne
class Professeur(Personne):
    def __init__(self, nom, age):
        super().__init__(nom, age)

    def enseigner(self):
        print("Je commence à enseigner.")

    def bonjour(self):
        super().bonjour()  # Appel à la méthode bonjour de la classe Personne
        print("Je suis un professeur.")

# Création d'un objet Eleve et appel des méthodes
eleve = Eleve("Alice", 14)
eleve.bonjour()
eleve.allerEnCours()

# Redéfinir l'âge de l'élève
eleve.age = 15
print(f"Après modification, {eleve.nom} a {eleve.age} ans.")

# Création d'un objet Professeur et appel des méthodes
professeur = Professeur("M. Dupont", 40)
professeur.bonjour()
professeur.enseigner()
