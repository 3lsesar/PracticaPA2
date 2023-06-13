from par_crom import ParellCromosomes

class Individu:

    def __init__(self, id, pcrom):
        self.__id = id
        self.__pcrom = pcrom
        self.__trets = []
    
    def get_id(self):
        return self.__id

    def get_pcrom(self):
        return self.__pcrom
    
    def afegir_tret(self, tret):
        self.__trets.append(tret)

    def treure_tret(self, tret):
        self.__trets.remove(tret)

    def get_trets(self):
        return self.__trets
    
    def consulta_individu(self):
        print(' ', self.__pcrom.get_prim())
        print(' ', self.__pcrom.get_seg())