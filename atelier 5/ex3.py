'''Définir  une  classe Rectangle avec un constructeur donnant des valeurs (longueur et largeur)  par  défaut et  un  attribut nom  =  "rectangle", une  méthode 
d'affichage et une méthode surface renvoyant la surface d'une instance. 
Définir une classe Carre héritant  de Rectangle et qui surcharge l'attribut d'instance : nom = "carré".'''

# classes
class Rectangle:
        """classe des rectangles."""

        def __init__(self, long=24, larg=27):
                "Initialisation avec valeurs par defaut"
                self.lon = long
                self.lar = larg
                self.nom = "rectangle"

        def surface(self):
                "Retourne la surface d'un rectangle."
                return self.lon*self.lar

        def __str__(self):
                "Affichage des caracteristiques d'un rectangle."
                return ("\nLe {0} de côtes {1} et {2} a une surface de {3}".format(self.nom, self.lon, self.lar, self.surface()))

class Carre(Rectangle):
        """classe des carres (herite de Rectangle)."""

        def __init__(self, cote=10):
                "Constructeur avec valeur par defaut"
                Rectangle.__init__(self, cote, cote)
                self.nom = "carre" # surchage d'attribut d'instance

# testing
if __name__ == '__main__':
        r = Rectangle(12, 8)
        print(r)
        c = Carre()
        print(c)