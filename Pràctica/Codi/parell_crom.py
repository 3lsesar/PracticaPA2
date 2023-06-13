class ParellCromosomes:

    def __init__(self, parellcrom):
        self.__m = len(parellcrom)//2
        self.__primer = parellcrom[:self.__m]
        self.__segon = parellcrom[self.__m:]

    def parelles_gens(self):
        llista_parelles = []
        for i in range(self.__m):
            llista_parelles.append((self.__primer[i], self.__segon[i]))
        return llista_parelles
            
    def consulta_individu(self):
        print(' ', self.__primer)
        print(' ', self.__segon)

    def get_prim(self):
        return self.__primer
    
    def get_seg(self):
        return self.__segon