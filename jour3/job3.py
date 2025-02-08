class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"Tâche: {self.titre}, Description: {self.description}, Statut: {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        """Ajoute une tâche à la liste."""
        self.taches.append(tache)

    def supprimerTache(self, tache):
        """Supprime une tâche de la liste."""
        if tache in self.taches:
            self.taches.remove(tache)

    def marquerCommeFinie(self, tache):
        """Marque une tâche comme terminée."""
        if tache in self.taches:
            tache.statut = "terminée"

    def afficherListe(self):
        """Affiche la liste complète des tâches."""
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        """Filtre les tâches par statut."""
        return [tache for tache in self.taches if tache.statut == statut]

# Test du code

# Création de plusieurs tâches
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser les cours", "Réviser pour l'examen de Python")
tache3 = Tache("Aller à la salle de sport", "Séance de musculation")

# Création de la liste de tâches
liste = ListeDeTaches()

# Ajouter les tâches à la liste
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

# Afficher toutes les tâches
print("Toutes les tâches:")
liste.afficherListe()

# Marquer une tâche comme terminée
liste.marquerCommeFinie(tache1)

# Afficher les tâches terminées
print("\nTâches terminées:")
liste.afficherListe()

# Filtrer et afficher les tâches "à faire"
print("\nTâches à faire:")
taches_a_faire = liste.filterListe("à faire")
for tache in taches_a_faire:
    print(tache)

# Supprimer une tâche
liste.supprimerTache(tache2)

# Afficher les tâches restantes
print("\nTâches restantes après suppression:")
liste.afficherListe()
