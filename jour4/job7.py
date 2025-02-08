import random

# Classe représentant une carte de jeu
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

    def valeur_numerique(self):
        # Si c'est un As, on retourne une valeur de 1 ou 11
        if self.valeur == 'As':
            return 1
        # Si c'est une figure (Valet, Dame, Roi), la valeur est 10
        elif self.valeur in ['Valet', 'Dame', 'Roi']:
            return 10
        # Sinon, on retourne la valeur numérique de la carte
        return int(self.valeur)

# Classe représentant le jeu de Blackjack
class Jeu:
    def __init__(self):
        self.paquet = []
        self.joueur_main = []
        self.croupier_main = []
        self.creer_paquet()
        self.melanger_paquet()

    def creer_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']

        # Créer toutes les cartes du paquet
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger_paquet(self):
        # Mélanger le paquet de cartes
        random.shuffle(self.paquet)

    def distribuer_carte(self, main):
        # Distribuer une carte à une main (joueur ou croupier)
        carte = self.paquet.pop()
        main.append(carte)

    def valeur_main(self, main):
        # Calculer la valeur d'une main (en prenant en compte les As)
        total = 0
        as_count = 0
        for carte in main:
            total += carte.valeur_numerique()
            if carte.valeur == 'As':
                as_count += 1

        # Ajuster la valeur des As si nécessaire
        while as_count > 0 and total <= 11:
            total += 10
            as_count -= 1

        return total

    def afficher_main(self, main, joueur):
        # Afficher les cartes de la main
        if joueur:
            print("Votre main:")
        else:
            print("Main du croupier:")
        for carte in main:
            print(carte)
        print("Valeur totale:", self.valeur_main(main))

    def tour_joueur(self):
        # Tour du joueur
        while True:
            self.afficher_main(self.joueur_main, joueur=True)
            choix = input("Souhaitez-vous 'prendre' une carte ou 'passer' ? ").lower()
            if choix == 'prendre':
                self.distribuer_carte(self.joueur_main)
                if self.valeur_main(self.joueur_main) > 21:
                    print("Vous avez dépassé 21 ! Vous avez perdu.")
                    return False
            elif choix == 'passer':
                break
            else:
                print("Choix invalide, veuillez entrer 'prendre' ou 'passer'.")
        return True

    def tour_croupier(self):
        # Tour du croupier
        while self.valeur_main(self.croupier_main) < 17:
            self.distribuer_carte(self.croupier_main)
        self.afficher_main(self.croupier_main, joueur=False)

    def determiner_gagnant(self):
        # Déterminer le gagnant en comparant les mains
        joueur_points = self.valeur_main(self.joueur_main)
        croupier_points = self.valeur_main(self.croupier_main)

        if joueur_points > 21:
            print("Vous avez perdu, vous avez dépassé 21 points.")
        elif croupier_points > 21 or joueur_points > croupier_points:
            print("Vous avez gagné !")
        elif joueur_points < croupier_points:
            print("Le croupier a gagné.")
        else:
            print("Égalité.")

    def jouer(self):
        # Début de la partie
        print("Bienvenue au Blackjack !")
        # Distribuer deux cartes au joueur et au croupier
        for _ in range(2):
            self.distribuer_carte(self.joueur_main)
            self.distribuer_carte(self.croupier_main)

        # Tour du joueur
        if not self.tour_joueur():
            return

        # Tour du croupier
        self.tour_croupier()

        # Déterminer le gagnant
        self.determiner_gagnant()

# Lancer une partie
jeu = Jeu()
jeu.jouer()
