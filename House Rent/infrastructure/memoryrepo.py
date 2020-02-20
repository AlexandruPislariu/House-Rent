from exceptii.erori import RepoError
class Repo():
#Repository din memorie, pe lista  
    def __init__(self):
        self.__lista_entitati = []
        
    def cauta_entitate(self,entitate):
        """
    Functia cauta o entitate in lista
        """
        for el in self.__lista_entitati:
            if int(el.get_id()) == int(entitate.get_id()):
                return self.__lista_entitati.index(el)
        
        return -1
    
    def adauga_entitate(self,entitate):
        
        index = self.cauta_entitate(entitate)
        if index!=-1:
            raise RepoError("Exista deja o entitate cu acest ID!")
        
        
        self.__lista_entitati.append(entitate)
        return self.__lista_entitati
       
    def get_entitate(self,index):
        
        return self.__lista_entitati[index] 
    
    def get_all(self):
        """
    Functia returneaza lista entitatilor
        """
        return self.__lista_entitati