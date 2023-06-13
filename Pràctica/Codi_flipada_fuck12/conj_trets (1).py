from par_crom import ParellCromosomes
from individu import Individu
from conj_ind import ConjuntIndividus

class ConjuntTrets:

    def __init__(self):
        self.__parelles = {}

    #Fer els canvis que això comporti
    def _parelles_gens(self, pcrom):
        llista_parelles = []
        m = pcrom.get_m()
        for i in range(m):
            llista_parelles.append((pcrom.get_prim()[i], pcrom.get_seg()[i]))
        return llista_parelles

    def _interseccio(self, pcrom1, pcrom2):
        ll_p1 = self._parelles_gens(pcrom1)
        ll_p2 = self._parelles_gens(pcrom2)
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
        
    # ind és una instància d'Individu
    def afegir_tret(self, tret, ind):

        if tret not in self.__parelles:
            self.__parelles[tret] = [ind.get_pcrom(), {ind}]
            ind.afegir_tret(tret)
        
        elif ind in self.__parelles[tret][1]:
            print("  error")   # <----- No sabem si print o return

        else:
            self.__parelles[tret][0] = self._interseccio(self.__parelles[tret][0], ind.get_pcrom())
            self.__parelles[tret][1].add(ind)
            ind.afegir_tret(tret)

    def treure_tret(self, tret, ind):
        ll_trets = ind.get_trets()
        if tret not in ll_trets:
            print("  error")   # <----- No sabem si print o return


        elif len(self.__parelles[tret][1]) == 1:
            self.__parelles.pop(tret)
            ind.treure_tret(tret)

        else:
            self.__parelles[tret][1].remove(ind)
            ll_ind = []
            for i in self.__parelles[tret][1]:
                ll_ind.append(i)
                i.treure_tret(tret)
            self.__parelles.pop(tret)
            for i in ll_ind:
                self.afegir_tret(tret, i)
                ind.afegir_tret(tret)

    # metode que, donat el nom d'un tret retorna 
    def consultar_tret(self,tret):
        if tret not in self.__parelles:
            print("  error")
            return False
        
        else:
            tret_desitjat = self.__parelles[tret]
            ll_id = []
            for i in tret_desitjat[1]:
                ll_id.append(i.get_id())
            print(' ', tret)
            print(' ', tret_desitjat[0].get_prim())
            print(' ', tret_desitjat[0].get_seg())
            for i in sorted(ll_id):
                print(' ', i)
    
    def llista_ind_tret(self,tret):
        if tret not in self.__parelles:
            return False
        
        else:
            ind_set = self.__parelles[tret][1]
            individus_id = ""
            for individu in ind_set:
                individus_id += str(individu.get_id())
            
            return individus_id 
            