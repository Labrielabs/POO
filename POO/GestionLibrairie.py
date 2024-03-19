"""
Écrivez une classe Livre pour représenter un livre dans une librairie. Chaque livre devrait avoir les attributs suivants :
Titre
Auteur
Genre
Prix
"""

# La classe Livre devrait également avoir les méthodes suivantes :

# Un constructeur pour initialiser les attributs du livre.
class Livre:
    def __init__(self, titre, auteur, genre, prix):
        self.__titre = titre
        self.__auteur = auteur
        self.genre = genre
        self.__prix = prix

    # Méthodes getters et setters pour chaque attribut
    def get_titre(self):
        return self.__titre

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def get_genre(self):
        return self.genre

    def set_genre(self, nouveau_genre):
        self.genre = nouveau_genre

    def get_prix(self):
        return self.__prix

    def set_prix(self, nouveau_prix):
        self.__prix = nouveau_prix

#Une méthode afficher_details() pour afficher les détails du livre (titre, auteur, genre, prix)
    def afficher_details(self):
        print(f"Titre : {self.__titre}")
        print(f"Auteur : {self.__auteur}")
        print(f"Genre : {self.genre}")
        print(f"Prix : {self.__prix} $")
# Ensuite, créez une classe Librairie pour représenter une collection de livres. La classe Librairie devrait avoir les attributs suivants :
        
class Librairie:
    def __init__(self):
        self.collection_livres = {}  # Dictionnaire pour stocker les livres,

#où la clé est le titre du livre et la valeur est une instance de la classe Livre.
    def ajouter_livre(self, livre):   #Une méthode ajouter_livre() pour ajouter un livre à la collection.
        self.collection_livres[livre.get_titre()] = livre

    def supprimer_livre(self, titre):   # Une méthode supprimer_livre() pour supprimer un livre de la collection.
        if titre in self.collection_livres:
            del self.collection_livres[titre]
            print(f"Le livre '{titre}' a été supprimé de la collection.")
        else:
            print(f"Le livre '{titre}' n'existe pas dans la collection.")

    def chercher_livre(self, titre):   # Une méthode chercher_livre() pour rechercher un livre par son titre et afficher ses détails.
        if titre in self.collection_livres:
            livre = self.collection_livres[titre]
            livre.afficher_details()
        else:
            print(f"Le livre '{titre}' n'existe pas dans la collection.")

# Exemple d'utilisation
librairie = Librairie()

# Ajout de livres
livre1 = Livre("Stéphane...Ma vie, My life", "Stéphane Labrie", "Science-Fiction", 125)
livre2 = Livre("Le Petit Prince de Makiavel", "Sun Tzu", "Stratégie Millitaire pour enfants", 115)
librairie.ajouter_livre(livre1)
librairie.ajouter_livre(livre2)

# Affichage des détails d'un livre
librairie.chercher_livre("Stéphane...Ma vie, My life")

# Suppression d'un livre
librairie.supprimer_livre("Le Petit Prince de Makiavel")

# Recherche d'un livre inexistant
librairie.chercher_livre("Rachid Narnia")
