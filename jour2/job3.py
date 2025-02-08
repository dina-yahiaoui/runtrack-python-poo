class Livre:
  def __init__(self, titre, auteur):
    self.titre = titre
    self.auteur = auteur
    self.__disponible = True  # Attribut privé

  def verification(self):
    return self.__disponible

  def emprunter(self):
    if self.verification():  # Vérifie si le livre est disponible
      self.__disponible = False
      print(f"Le livre '{self.titre}' a été emprunté.")
    else:
        print(f"Le livre '{self.titre}' n'est pas disponible pour l'emprunt.")

  def rendre(self):
    if not self.verification():  # Vérifie si le livre a été emprunté
      self.__disponible = True
      print(f"Le livre '{self.titre}' a été rendu.")
    else:
      print(f"Le livre '{self.titre}' n'a pas été emprunté.")
