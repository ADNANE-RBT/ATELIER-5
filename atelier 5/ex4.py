'''Définir une classe Point avec un constructeur fournissant les coordonnées par défaut d'un point du plan (par exemple : x = 0.0 et y = 0.0). 
Définir une classe Segment dont le constructeur possède quatre paramètres : deux pour  l'origine  et  deux  pour  l'extrémité. 
Ce  constructeur définit deux attributs : orig et extrem, instances de la classe Point.
De cette manière, vous concevez une classe  composite  :  la  classe Segment est  composée  de  deux  instances  de  la  classe Point. 
Ajouter une méthode d'affichage. 
Enfin écrire un auto-test qui affiche une instance de Segment initialisée par les valeurs  1, 2, 3 et 4'''

class Point:
    """defintion du class"""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Segment:
    """defintion du class"""
    def __init__(self, originX, originY, extremeX, extremeY):
        self.origin = Point(originX,originY)
        self.extreme = Point(extremeX,extremeY)

    def printSegment(self):
        print("segment original: ({0},{1})".format(self.origin.x,self.origin.y))
        print("segment extreme: ({0},{1})".format(self.extreme.x,self.extreme.y))

# creation d'un instance

mySegment = Segment(1,2,3,4)
mySegment.printSegment()