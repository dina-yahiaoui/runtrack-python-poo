class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est : {self.age}")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def __init__(self, age=14):
        super().__init__(age)

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


# Instantiation de la classe Personne
personne = Personne()
personne.afficherAge()  # Affiche l'âge de la personne

# Instantiation de la classe Eleve
eleve = Eleve()
eleve.afficherAge()  # Affiche l'âge par défaut de l'élève
