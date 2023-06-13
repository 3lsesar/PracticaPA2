from pytokr import item
from bintree import BinTree
from individu import Individu
from par_crom import ParellCromosomes

def ll_id_esq(self, arbre, ll_id, ll_nova = []):
        arrel = arbre.get_root()
        if arrel in ll_id:
            ll_nova.append(arrel)
        ll_id_esq(arbre.get_left(), ll_id)
        ll_id_esq(arbre.get_right(), ll_id)
        return ll_nova

def ll_id_dre(self, arbre, ll_id, ll_nova = []):
        arrel = arbre.get_root()
        if arrel in ll_id:
            ll_nova.append(arrel)
        esq = arbre.get_left()
        
        return ll_nova + [ll_id_esqdre(arbre.get_left())] + [ll_id_esqdre(arbre.get_left())]

d = BinTree('5')
c = BinTree('4')
b = BinTree('1', left = c)
a = BinTree('3', left = b, right = d)
ll_id = ['4', '5']
print(ll_id_esqdre(b, ll_id))


