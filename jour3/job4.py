class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"{self.nom} ({self.numero}, {self.position})")
        print(f"Buts marqués : {self.buts}")
        print(f"Passes décisives : {self.passes_decisives}")
        print(f"Cartons jaunes : {self.cartons_jaunes}")
        print(f"Cartons rouges : {self.cartons_rouges}")
        print("-----")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de l'équipe {self.nom}:")
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur_nom, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == joueur_nom:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton_jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton_rouge":
                    joueur.recevoirUnCartonRouge()

# Création de joueurs
joueur1 = Joueur("John Doe", 10, "Attaquant")
joueur2 = Joueur("Marc Dupont", 7, "Milieu")
joueur3 = Joueur("Pierre Martin", 5, "Défenseur")

# Création d'une équipe et ajout des joueurs
equipe = Equipe("FC Paris")
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe.ajouterJoueur(joueur3)

# Affichage des statistiques initiales
equipe.afficherStatistiquesJoueurs()

# Simulation d'un match
equipe.mettreAJourStatistiquesJoueur("John Doe", "but")
equipe.mettreAJourStatistiquesJoueur("Marc Dupont", "passe")
equipe.mettreAJourStatistiquesJoueur("Pierre Martin", "carton_jaune")
equipe.mettreAJourStatistiquesJoueur("John Doe", "carton_rouge")

# Affichage des statistiques après mise à jour
equipe.afficherStatistiquesJoueurs()

