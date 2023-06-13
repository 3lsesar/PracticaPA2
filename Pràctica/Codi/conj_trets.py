from individu import Individu
from parell_crom import ParellCromosomes

class ConjuntTrets:

    def __init__(self):
        self.__parelles = {}

    def interseccio(self, p1, p2):
        ll_p1 = p1.parelles_gens()
        ll_p2 = p2.parelles_gens()
        primer = []
        segon = []
        for i in range(len(ll_p1)):
            if ll_p1[i] == ll_p2[i]:
                primer.append(ll_p1[i][0])
                segon.append(ll_p1[i][1])
            else:
                primer.append("-")
                segon.append("-")
        junt = primer + segon
        result = ''.join(str(x) for x in junt)
        return ParellCromosomes(result)
        
    #inst_pcrom i ind són instàncies ParellCromosomes i Individu, respectivament
    def afegir_tret(self, tret, pcrom, ind):
        if tret not in self.__parelles:
            self.__parelles[tret] = pcrom, {ind}

        elif ind in self.__parelles[tret][1]:
            print("error")   # <----- No sabem si print o return
        
        else:
            self.__parelles[tret][0] = self.interseccio(self.__parelles[tret][0], pcrom)
            self.__parelles[tret][1].add(ind)
    
    # metode que, dont el nom d'un tret retorna 
    """def consultar_tret(self,tret):
        if tret not in self.__parelles:
            print("error")
        tret_desitjat = self.__parelles[tret]
        return (tret_desitjat[0], tret_desitjat[1].sort())"""
    
    #No sabem si posar print o return
    def consultar_individu_tret(self, id):
        ll_trets = []
        ll_claus = list(self.__parelles.keys())
        for i in ll_claus:
            if id in self.__parelles[i][1]:
                ll_trets.append(i)
        if ll_trets != []:
            for i in ll_trets:
                print(' ', i)
    
