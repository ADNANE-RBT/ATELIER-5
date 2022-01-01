#Définir une classe Vecteur2D avec un constructeur fournissant les coordonnées par défaut d’un vecteur du plan (par exemple : x = 0 et y = 0)

# classe
class Vecteur2D:
        """Les Vecteurs plans."""
        def __init__(self, X=0, Y=0):
                """Constructeur avec des  parametres par defaut."""
                self.a = X # initialisation de a et b, attributs d'instance
                self.b = Y
                self.nom = "adnane riyadi"
        def affiche(self):
                print (self.nom)
        def __str__(self):
                """ Utilisation du print """
                return "x = %d, y = %d" % (self.a,self.b)

# Auto-test ---------------------------------------------------------
if __name__ == '__main__':
        print(" une instance par defaut est ")
        print (Vecteur2D())
        Vecteur2D().affiche()

        print("\n")

        print(" une instance initialise est ")
        print (Vecteur2D(-666, 777))
        Vecteur2D().affiche()