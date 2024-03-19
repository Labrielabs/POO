class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.solde = solde_initial

    def depot(self, montant):
        try:
            montant = float(montant)
            if montant > 0:
                self.solde += montant
                print(f"Montant de {montant} $ déposé. KA-CHING!!! Nouveau solde : {self.solde} $")
            else:
                print("Erreur : Le montant doit être positif, c'est pas l'Armée du salut ici...")
        except ValueError:
            print("Erreur : Veuillez entrer un montant valide.")

    def retrait(self, montant):
        try:
            montant = float(montant)
            if 0 < montant <= self.solde:
                self.solde -= montant
                print(f"Montant de {montant} $ retiré. KA-CHING!!! Nouveau solde : {self.solde} $   Dépenses pas tout à la même place...")
            else:
                print("Erreur Yo! : Soit le montant est mal entré ou soit t'es broke chum...")
        except ValueError:
            print("Erreur : Check tes affaires, on dirait que t'as mal entré tes chiffres.")

    def verifier_solde(self):
        print(f"Solde actuel : {self.solde} $")

# Exemple d'utilisation
if __name__ == "__main__":
    compte = CompteBancaire(100)  # Crée un compte avec un solde initial de 100 $
    montant_depot = input("Combien voulez-vous déposer ? : ")
    compte.depot(montant_depot)  # Dépose le montant saisi
    montant_retrait = input("Combien voulez-vous retirer ? : ")
    compte.retrait(montant_retrait)  # Retire le montant saisi
    compte.verifier_solde()  # Affiche le solde actuel