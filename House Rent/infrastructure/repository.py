from infrastructure.memoryrepo import Repo

class RepositoryFile(object):
#repository din fisier   
    
    def __init__(self, filename, entity):
        self.__filename = filename
        self.__entity = entity
        self.__repo = Repo()
        self.__read_all_from_file()
        
    def __read_all_from_file(self):
        """
    FUnctia incarca tot stocul de inchirieri din fisier
        """
        fh = open(self.__filename,'r')
        content = fh.read()
        
        content = content.split('\n')
        
        for line in content:
            if line.strip()=='':
                continue
            entitate = self.__entity.read_entity(line) #transform continutul in entitate
            self.__repo.adauga_entitate(entitate) #adaug in repository
            
    def __write_all_in_file(self):
        """
    Functia scrie in fisier inchrierile in memorie
        """
        fh = open(self.__filename,'a')
      
    #curat continutul  
        fh.seek(0)
        fh.truncate()
        
    #rescriu
        produse = self.__repo.get_all()
        for el in produse:
            fh.write(self.__entity.write_entity(el))
            fh.write('\n')
            
    def adauga_entitate(self,entitate):
        
        self.__repo.adauga_entitate(entitate)
        self.__write_all_in_file()
      
    def cauta_entitate(self,entitate):
        
        return self.__repo.cauta_entitate(entitate)
    
    def get_entitate(self,index):
        
        return self.__repo.get_entitate(index)
              
    def get_all(self):
        
        return self.__repo.get_all() 
        
            
        
    



