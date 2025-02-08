class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    def ajouter_habitant(self):
        self.__habitants += 1

    def get_habitants(self):
        return self.__habitants

    def get_nom(self):
        return self.__nom


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville.ajouter_habitant()


# Création des objets Ville
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage du nombre initial d'habitants
print(f"Nombre d'habitants à Paris: {paris.get_habitants()}")
print(f"Nombre d'habitants à Marseille: {marseille.get_habitants()}")

# Création des objets Personne
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage du nombre d'habitants après l'arrivée des nouvelles personnes
print(f"Nombre d'habitants à Paris après l'arrivée de John et Myrtille: {paris.get_habitants()}")
print(f"Nombre d'habitants à Marseille après l'arrivée de Chloé: {marseille.get_habitants()}")
