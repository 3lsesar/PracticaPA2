from pytokr import item
from bintree import BinTree
from individu import Individu
from par_crom import ParellCromosomes

class ConjuntIndividus:
    def __init__(self):
        self.__llista = [None]
    
    #ind és una instància d'Individu
    def afegir_ind(self, ind):
        self.__llista.append(ind)

    def get_llista(self):
        return self.__llista
    
    def llegeix_bintree_int(self, marca):
        x = int(item())
        if x != marca:
            l = self.llegeix_bintree_int(marca)
            r = self.llegeix_bintree_int(marca)
            return BinTree(x,l,r)
        else:
            return BinTree()
        
    def get_bintree(self):
        tree = self.llegeix_bintree_int(0)
        return tree
    
    def llegir_ind(self, n):
        for i in range(n):
            inst_pcrom = ParellCromosomes(item())
            inst_ind = Individu(i + 1, inst_pcrom)
            self.afegir_ind(inst_ind)
        return self.get_llista()
    
    def dist_tret(self, tree, individus):
        
        print("hola mis bubus de youtube")

        if individus == False:
            print("error")
            return None
        
    
        
        elif str(tree.get_root()) not in individus:
            
            if tree.get_right().empty() == True:
                r = None
            else:
                r = self.dist_tret(tree.get_right(),individus)
            
            if tree.get_left().empty() == True:
                l = None
            
            else:
                l = self.dist_tret(tree.get_left(),individus)

            return r,l
            
        
        else:
            result =""
            ino = tree.inorder()
            for i in ino:
                if str(i) in individus:
                    result += str(i)
            
            print(result)
            return None
        
