from pytokr import item
from bintree import BinTree
from individu import Individu
from par_crom import ParellCromosomes
from copy import deepcopy

class ConjuntIndividus:
    def __init__(self):
        self.__llista = [None]
        self.__arbre = self.llegeix_bintree_int(0)
    
    # ind és una instància d'Individu
    def afegir_ind(self, ind):
        self.__llista.append(ind)

    def get_llista(self):
        return self.__llista
    
    def llegir_ind(self, n):
        for i in range(n):
            inst_pcrom = ParellCromosomes(item())
            inst_ind = Individu(i + 1, inst_pcrom)
            self.afegir_ind(inst_ind)
        return self.get_llista()
    
    def llegeix_bintree_int(self, marca):
        x = int(item())
        if x != marca:
            l = self.llegeix_bintree_int(marca)
            r = self.llegeix_bintree_int(marca)
            return BinTree(x,l,r)
        else:
            return BinTree()

    def _ll_id_esqdre(self, arbre, ll_id, ll_nova = None):
        if ll_nova == None:
            ll_nova = []
        if arbre.empty():
            return []
        else:
            arrel = arbre.get_root()
            if arrel in ll_id:
                ll_nova.append(arrel)
            self._ll_id_esqdre(arbre.get_left(), ll_id, ll_nova)
            self._ll_id_esqdre(arbre.get_right(), ll_id, ll_nova)
            return ll_nova
  
    def subarbre(self, arbre, ll_id):
        if ll_id == []:
            return BinTree()
        elif arbre.get_root() in ll_id and len(ll_id) == 1:
            return BinTree(arbre.get_root())
        else:
            ll_l = self._ll_id_esqdre(arbre.get_left(), ll_id)
            ll_r = self._ll_id_esqdre(arbre.get_right(), ll_id)
            l = self.subarbre(arbre.get_left(), ll_l)
            r = self.subarbre(arbre.get_right(), ll_r)
            return BinTree(arbre.get_root(), l, r)
        
    def ind_trets(self, ll_id):
        ll_nova = []
        subarbre = self.subarbre(self.__arbre, ll_id).inorder()
        for i in subarbre:
            if i in ll_id:
                ll_nova.append(i)
            else:
                ll_nova.append(-i)
        return ll_nova
    
    # Quan la llista és més gran que 1 passa algo raro
    def inorder(self, ll_id):
        arbre_inorder = self.ind_trets(ll_id)
        print('  ', end='')
        for i in arbre_inorder:
            print(i, ' ', end='')
        print()

e = BinTree(2)
d = BinTree(5)
c = BinTree(4)
b = BinTree(1, left = c, right = e)
a = BinTree(3, left = b, right = d)
ll_id = [2]