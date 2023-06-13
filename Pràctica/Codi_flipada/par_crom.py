class ParellCromosomes:

    def __init__(self, pcrom):
        self.__m = len(pcrom)//2
        self.__primer = pcrom[:self.__m]
        self.__segon = pcrom[self.__m:]

    def get_prim(self):
        return self.__primer
    
    def get_seg(self):
        return self.__segon
    
    def get_m(self):
        return self.__m