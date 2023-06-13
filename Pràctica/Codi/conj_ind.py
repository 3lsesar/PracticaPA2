from bintree import BinTree
from individu import Individu

class ConjuntIndividus:
    def __init__(self,tree):
        self.tree = tree
    
    def llista_individus(self,n):
        instancies_ind = [None]
        
        for i in range(n):
            instancies_ind.append(Individu(i+1))
        
        return instancies_ind

