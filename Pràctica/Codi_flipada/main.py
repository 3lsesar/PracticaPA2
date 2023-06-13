from pytokr import item
from bintree import BinTree
from par_crom import ParellCromosomes
from conj_ind import ConjuntIndividus
from conj_trets import ConjuntTrets
from individu import Individu

instruccio = item()

while instruccio != 'fi':

    #No tinc clar quan posar els prints (principi o final?)
    if instruccio == 'experiment':
        n = int(item())
        m = int(item())

        conj_ind = ConjuntIndividus()
        tree = conj_ind.get_bintree()
        ll_ind = conj_ind.llegir_ind(n)
        conjunt_trets = ConjuntTrets()
        print("experiment",n,m)

    elif instruccio == 'afegir_tret':
        tret = item()
        id = int(item())
        ind = ll_ind[id]
        print('afegir_tret', tret, id)
        conjunt_trets.afegir_tret(tret, ind)
    
    elif instruccio == 'treure_tret':
        tret = item()
        id = int(item())
        ind = ll_ind[id]
        print('treure_tret', tret, id)
        conjunt_trets.treure_tret(tret, ind)

    elif instruccio == 'consulta_tret':
        tret = item()
        print('consulta_tret', tret)
        conjunt_trets.consultar_tret(tret)
    
    elif instruccio == 'consulta_individu':
        id = int(item())
        ind = ll_ind[id]
        print('consulta_individu', id)
        ind.consulta_individu()
        ll_trets = ind.get_trets()
        #No és segur això
        if ll_trets != []:
            for i in ll_trets:
                print(' ', i)

    elif instruccio == 'distribucio_tret':
        pass
    
    instruccio = item()

