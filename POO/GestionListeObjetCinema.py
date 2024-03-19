"""
Simulation d'un système de réservation
"""

# Créez une classe SalleCinema pour gérer les réservations dans une salle de cinéma.
class SalleCinema: 
    def __init__(self, capacite):
        self.capacite = capacite
        self.places_reservees = {}  # Dictionnaire pour stocker les réservations
# Modifiez la classe SalleCinema pour qu'elle puisse gérer des places spéciales pour les personnes handicapées.
        self.places_speciales = set()  # Ensemble pour stocker les places spéciales

# Ajoutez une méthode reserver_place(nom, place) pour réserver une place pour une personne.
# Ajoutez une vérification dans la méthode reserver_place(nom, place) pour s'assurer 
# qu'il reste des places disponibles avant de réserver.       
    def reserver_place(self, nom, place):
        if len(self.places_reservees) >= self.capacite: # Vérification des places disponibles
            print("Désolé, il n'y a plus de places disponibles.")
        elif place in self.places_reservees:
            print(f"La place {place} est déjà réservée.")
        elif place in self.places_speciales:
            print(f"La place {place} est spéciale et ne peut pas être réservée.")
        else:
            self.places_reservees[place] = nom
            print(f"{nom} a réservé la place {place}.")

# Ajoutez une méthode afficher_places_reservées() pour afficher les places réservées.
    def afficher_places_reservées(self):
        print("Places réservées :")
        for place, nom in self.places_reservees.items():
            print(f"Place {place} : {nom}")

# Ajoutez une méthode nombre_places_disponibles() à la classe
# SalleCinema pour afficher le nombre de places disponibles.           
    def nombre_places_disponibles(self):
        places_disponibles = self.capacite - len(self.places_reservees)
        print(f"Nombre de places disponibles : {places_disponibles}")

# Ajoutez une méthode filtrer_reservations_par_personne(nom) à la classe SalleCinema pour 
# afficher les réservations faites par une personne spécifique.
    def filtrer_reservations_par_personne(self, nom):
        print(f"Réservations faites par {nom} :")
        for place, personne in self.places_reservees.items():
            if personne == nom:
                print(f"Place {place}")

# Ajoutez une méthode annuler_reservation(nom) à la classe SalleCinema pour annuler toutes les réservations 
# faites par une personne spécifique.
    def annuler_reservation(self, nom):
        places_annulees = [place for place, personne in self.places_reservees.items() if personne == nom]
        for place in places_annulees:
            del self.places_reservees[place]
        print(f"Réservations de {nom} annulées pour les places : {', '.join(map(str, places_annulees))}")

# Ajoutez une méthode reserver_place_speciale(nom) pour réserver une place spéciale pour une personne handicapée.
    def reserver_place_speciale(self, nom, place):
        self.places_speciales.add(place)
        print(f"{nom} a réservé la place spéciale {place}.")

# Exemple d'utilisation
salle = SalleCinema(capacite=50)

salle.reserver_place("Hugo", place=10)
salle.reserver_place("Mireille", place=20)
salle.reserver_place("Yvon", place=10)  # Place déjà réservée
salle.reserver_place("Jean-Guy", place=30)  # Place spéciale

salle.afficher_places_reservées()
salle.nombre_places_disponibles()
salle.filtrer_reservations_par_personne("Hugo")
salle.annuler_reservation("Mireille")
salle.reserver_place_speciale("Jean-Guy", place=5)
