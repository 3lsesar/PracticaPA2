from pytokr import item
from bintree import BinTree
from parell_crom import ParellCromosomes
from conj_ind import ConjuntIndividus
from conj_trets import ConjuntTrets
from individu import Individu

def llegeix_bintree_int(marca):
        x = int(item())
        if x != marca:
            l = llegeix_bintree_int(marca)
            r = llegeix_bintree_int(marca)
            return BinTree(x,l,r)
        else:
            return BinTree()

def instancies_pcrom():
    ll_pcrom = [None]
    for i in range(n):
        inst_pcrom = ParellCromosomes(item())
        ll_pcrom.append(inst_pcrom)
    return ll_pcrom
    
instruccio = item()

while instruccio != 'fi':

    #No tinc clar quan posar els prints (principi o final?)
    if instruccio == 'experiment':
        n = int(item())
        m = int(item())

        individus = ConjuntIndividus(llegeix_bintree_int(0))
        ll_pcrom = instancies_pcrom()
        ll_ind = individus.llista_individus(n)
        conjunt_trets = ConjuntTrets()
        print("experiment",n,m)

    elif instruccio == 'afegir_tret':
        nom_tret = item()
        id_individu = int(item())
        ind = ll_ind[id_individu]
        pcrom = ll_pcrom[id_individu]
        print('afegir_tret', nom_tret, ' ', id_individu)
        conjunt_trets.afegir_tret(nom_tret, pcrom, ind)
    
    elif instruccio == 'treure_tret':
        pass

    elif instruccio == 'consulta_tret':
        pass
    
    elif instruccio == 'consulta_individu':
        individu = int(item())
        inst_ind = ll_ind[individu]
        print('consulta_individu', individu)
        ll_pcrom[individu].consulta_individu()
        conjunt_trets.consultar_individu_tret(inst_ind)

    elif instruccio == 'distribucio_tret':
        pass
    
    instruccio = item()