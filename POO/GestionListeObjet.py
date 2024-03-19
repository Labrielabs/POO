class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class ListePersonnes:
    def __init__(self):
        self.personnes = []  # Initialisation de la liste vide

    def ajouter_personne(self, nom, age):
        nouvelle_personne = Personne(nom, age)
        self.personnes.append(nouvelle_personne)

    def afficher_personnes(self):
        for personne in self.personnes:
            print(f"Nom : {personne.nom}, Âge : {personne.age}")

    def rechercher_personne(self, nom):
        for personne in self.personnes:
            if personne.nom.lower() == nom.lower():
                print(f"Personne trouvée : {personne.nom}, Âge : {personne.age}")
                return
        print(f"Aucune personne trouvée avec le nom : {nom}")
   
    def filtrer_personnes_par_age(self, min_age, max_age):
        personnes_filtrees = [personne for personne in self.personnes if min_age <= personne.age <= max_age]
        if personnes_filtrees:
            print("Personnes dont l'âge est compris entre {} et {} :".format(min_age, max_age))
            for personne in personnes_filtrees:
                print(f"Nom : {personne.nom}, Âge : {personne.age}")
        else:
            print(f"Aucune personne trouvée avec un âge entre {min_age} et {max_age}.")

# Créez une instance de ListePersonnes
liste_personnes = ListePersonnes()

# Ajoutez quelques personnes
liste_personnes.ajouter_personne("Junior", 22)
liste_personnes.ajouter_personne("Steeve", 27)
liste_personnes.ajouter_personne("Horace", 49)
liste_personnes.ajouter_personne("Hubert", 38)
liste_personnes.ajouter_personne("Maurice", 17)
liste_personnes.ajouter_personne("Rosaire", 89)
liste_personnes.ajouter_personne("Julie", 33)
liste_personnes.ajouter_personne("Johanna", 24)
liste_personnes.ajouter_personne("Nina", 41)


# Recherche d'une personne par nom
liste_personnes.rechercher_personne("Nina")
liste_personnes.rechercher_personne("Marjorie")  # Nom non trouvé

   
# Filtrer les personnes dont l'âge est entre 25 et 35
liste_personnes.filtrer_personnes_par_age(min_age=25, max_age=35)


class FileAttente:
    def __init__(self):
        self.file = []  # Initialisation de la file d'attente vide

    def ajouter_personne_en_attente(self, nom):
        self.file.append(nom)
        print(f"{nom} a été ajouté à la file d'attente.")

    def supprimer_personne_de_attente(self):
        if self.file:
            personne_supprimee = self.file.pop(0)
            print(f"{personne_supprimee} a été retiré(e) de la file d'attente.")
        else:
            print("La file d'attente est déjà vide.")

# Exemple d'utilisation
file_attente = FileAttente()
file_attente.ajouter_personne_en_attente("Mathieu")
file_attente.ajouter_personne_en_attente("Robert")
file_attente.ajouter_personne_en_attente("Guillaume")

# Supprimer la première personne de la file d'attente
file_attente.supprimer_personne_de_attente()

# Modification de la classe FileAttente pour qu'elle puisse gérer des personnes prioritaires.
class FileAttente:
    def __init__(self):
        self.file = []  # Initialisation de la file d'attente vide

    def ajouter_personne_en_attente(self, nom):
        self.file.append(nom)
        print(f"{nom} a été ajouté à la file d'attente.")

    def supprimer_personne_de_attente(self):
        if self.file:
            # Cherche d'abord une personne prioritaire
            for i, personne in enumerate(self.file):
                if personne.startswith("VIP_"):
                    personne_supprimee = self.file.pop(i)
                    print(f"{personne_supprimee} (prioritaire) a été retiré(e) de la file d'attente.")
                    return

            # Si aucune personne prioritaire n'est trouvée, supprime la première personne normale
            personne_supprimee = self.file.pop(0)
            print(f"{personne_supprimee} a été retiré(e) de la file d'attente.")
        else:
            print("La file d'attente est déjà vide.")

# Exemple d'utilisation
file_attente = FileAttente()
file_attente.ajouter_personne_en_attente("Rodrigo")
file_attente.ajouter_personne_en_attente("Fernando")
file_attente.ajouter_personne_en_attente("VIP_Carlito")

# Supprimer en priorité une personne prioritaire
file_attente.supprimer_personne_de_attente()







