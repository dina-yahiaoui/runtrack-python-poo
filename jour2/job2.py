class Livre:
    def __init__(self, titre: str, auteur: str, pages: int):
        self._titre = titre
        self._auteur = auteur
        self._pages = pages if isinstance(pages, int) and pages > 0 else 0
        if self._pages == 0:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    # Getter pour le titre
    def get_titre(self):
        return self._titre

    # Setter pour le titre
    def set_titre(self, titre: str):
        self._titre = titre

    # Getter pour l'auteur
    def get_auteur(self):
        return self._auteur

    # Setter pour l'auteur
    def set_auteur(self, auteur: str):
        self._auteur = auteur

    # Getter pour le nombre de pages
    def get_pages(self):
        return self._pages

    # Setter pour le nombre de pages avec vérification
    def set_pages(self, pages: int):
        if isinstance(pages, int) and pages > 0:
            self._pages = pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    # Affichage des informations du livre
    def afficher_livre(self):
        print(f"Titre : {self._titre}, Auteur : {self._auteur}, Pages : {self._pages}")

# Exemple d'utilisation
livre = Livre("1984", "George Orwell", 328)
livre.afficher_livre()

livre.set_pages(-50)  # Test de la validation
titre = livre.get_titre()
print("Titre du livre :", titre)