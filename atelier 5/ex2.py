#Enrichissez la classe Vecteur2D précédente en lui ajoutant une méthode d’affichage et une méthode de surcharge d’addition de deux vecteurs du plan. 
#Dans le programme principal, instanciez deux Vecteur2D, affichez-les et affichez leur somme

class Vecteur2D():
    #la class
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    #affichage des vecteurs
    def printVec(self):
        print('coordonne de cette vector: ({0},{1})'.format(self.x,self.y),"\n")

    #somme des 2 vecteurs 
    def __add__(self,next):
        result = Vecteur2D(self.x+next.x,self.y+next.y)
        return result


# instiation de Vecteur2d
v1 = Vecteur2D(12,34)
v2 = Vecteur2D(23,-6)

# affichage des deux vecteurs
v1.printVec()
v2.printVec()

# la somme des 2 vecteurs
som = v1 + v2
print('la somme de v1 et v2 est \n')
som.printVec()