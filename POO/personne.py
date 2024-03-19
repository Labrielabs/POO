
class Personne:
    """
    Cette classe Personne nous permet de représenter la conception d'une personne
    """
    personne_creee = 0
    # constructeur__init__()
    def __init__(self, nom, prenom, age): #-> None:
        self.__nom = nom # privé
        self.prenom = prenom # public
        self.__age = age # privé
        Personne.personne_creee +=1

    # Accéder à l'attribut âge à l'extérieur de la classe 
    def get_age(self):
        return self.__age
    
    # Mutateur de l'attribut age
    def set_age(self, age):
        self.__age = age
    
        #print("Personne crée : Cela veut dire qu'un objet personne a été créée ( ou instanciée ).")
        def infos(self):
            print(".........................................................")
            print(f"Nom: {self.__nom}, Prénom: {self.prenom}, Age: {self.__age}")

        

# main ---> Programme Principal
# Instanciation de la classe Personne --> création d'un objet de la classe Personne : p1 
print("---------------------------------------------------------------------")
p1 = Personne("Labrie", "Stephane", 25) #p1
p1.infos()
# Non reccommandé en POO, vaut mieux rendre les attributs privés avec le double underscore __
# Encapsulation ...
p1.set_age =(49)
print("Age access :", p1.get_age())
p1.prenom = "Jojo"
p1.__nom = "Bijou"
print("\nAprès modification de l'âge de Stéphane\n")
p1.infos()
p2 = Personne("Diallo", "Abdou", 14) #p2
p2.infos()
#p3 = Personne() #p3
#print(p1.__doc__)

print("---------------------------------------------------------------------")