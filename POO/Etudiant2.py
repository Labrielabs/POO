class Etudiant:
    etudiant_cree = 0
    def __init__(self, nom, prenom, sexe, naissance, specialite):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.naissance = naissance
        self.specialite = specialite
        Etudiant.etudiant_cree +=1
        print(f"Création de l'étudiant {Etudiant.etudiant_cree}")

    def infos(self):
        print("-----------------------------------------------------------------------------------------------------------------------")
        print(f"nom: {self.nom}, prenom: {self.prenom}, sexe: {self.sexe}, naissance: {self.naissance}, specialité: {self.specialite}")
        print("-----------------------------------------------------------------------------------------------------------------------")

e1 = Etudiant("Morino", "Jacques", "M", "1940-07-14", "Génie Civil")
e1.infos()

e2 = Etudiant("Barr", "Lenny", "M", "1992-09-29", "Chirurgien")
e2.infos()




