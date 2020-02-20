from domain.entitati import House,InchiriereDTO
class ServiceHouse(object):
#In aceasta clasa creez cele 2 functionalitati(statistici)    
    
    def __init__(self, repoHouse):
        self.__repoHouse = repoHouse
    
    def find_houses(self,locatie,numar_persoane):
        """
    Functia creeaza o lista cu toate casele din aceasta locatie care au o capacitate mai mare decat numarul de persoane
        """
        
        locuinte = self.__repoHouse.get_all() #preiau toate locuintele din baza de date
        
        lista = [] #lista caselor dinponibile locatie
        
        for house in locuinte:#cauta dupa preferinte
            if (locatie in house.get_locatie()) and (int(numar_persoane) <= int(house.get_capacitate())):
                lista.append(house)#adaug in lista casele care satisfac preferintele
                
        return lista
    
    def rent(self,id,numar_zile):
        """
    Functia returneaza casa si pretul inchrierii pentru numarul de zile introdus
        """
        
        locuinta = House(id,'asdas','asdas',20,100)
        index = self.__repoHouse.cauta_entitate(locuinta)#caut locuinta
        
        locuinta = self.__repoHouse.get_entitate(index)#preiau atributele
        
        return InchiriereDTO(locuinta.get_nume(),locuinta.get_locatie(),locuinta.get_capacitate(),int(numar_zile)*int(locuinta.get_pret_noapte()))


