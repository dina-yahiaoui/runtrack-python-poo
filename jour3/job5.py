import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        degats = random.randint(5, 15)  # Les dégâts varient entre 5 et 15
        adversaire.subir_degats(degats)
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} dégâts.")
    
    def subir_degats(self, degats):
        self.vie -= degats
    
    def est_vivant(self):
        return self.vie > 0
    
    def afficher_statistiques(self):
        print(f"{self.nom} - Vie: {self.vie}")
        
class Jeu:
    def __init__(self):
        self.niveau = 0
        self.joueur = None
        self.ennemi = None
    
    def choisirNiveau(self):
        print("Choisissez un niveau de difficulté :")
        print("1 - Facile")
        print("2 - Moyen")
        print("3 - Difficile")
        
        choix = int(input("Entrez le numéro du niveau: "))
        if choix == 1:
            self.niveau = 1
        elif choix == 2:
            self.niveau = 2
        elif choix == 3:
            self.niveau = 3
        else:
            print("Niveau invalide, par défaut niveau moyen.")
            self.niveau = 2
    
    def lancerJeu(self):
        if self.niveau == 1:
            joueur_vie = 50
            ennemi_vie = 40
        elif self.niveau == 2:
            joueur_vie = 60
            ennemi_vie = 60
        else:
            joueur_vie = 80
            ennemi_vie = 100
        
        self.joueur = Personnage("Joueur", joueur_vie)
        self.ennemi = Personnage("Ennemi", ennemi_vie)
        
        self.commencer_combat()
    
    def commencer_combat(self):
        print(f"\nDébut du combat : {self.joueur.nom} vs {self.ennemi.nom}")
        while self.joueur.est_vivant() and self.ennemi.est_vivant():
            self.joueur.afficher_statistiques()
            self.ennemi.afficher_statistiques()
            
            # Le joueur attaque
            self.joueur.attaquer(self.ennemi)
            if not self.ennemi.est_vivant():
                break
            
            # L'ennemi attaque
            self.ennemi.attaquer(self.joueur)
            if not self.joueur.est_vivant():
                break
        
        self.verifier_gagnant()
    
    def verifier_gagnant(self):
        if self.joueur.est_vivant():
            print("\nFélicitations, vous avez gagné !")
        else:
            print("\nVous avez perdu, l'ennemi a gagné.")
    
# Création du jeu et démarrage
jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
