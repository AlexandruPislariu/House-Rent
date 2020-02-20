class House():
#Prin aceasta clasa abstractizez o locuinta  
  
    def __init__(self,id,nume,locatie,capacitate,pret_noapte):
        self.__id = id
        self.__nume = nume
        self.__locatie = locatie
        self.__capacitate = capacitate
        self.__pret_noapte = pret_noapte

    def get_id(self):
        return self.__id


    def get_nume(self):
        return self.__nume


    def get_locatie(self):
        return self.__locatie


    def get_capacitate(self):
        return self.__capacitate


    def get_pret_noapte(self):
        return self.__pret_noapte


    def set_nume(self, value):
        self.__nume = value


    def set_locatie(self, value):
        self.__locatie = value


    def set_capacitate(self, value):
        self.__capacitate = value


    def set_pret_noapte(self, value):
        self.__pret_noapte = value

    @classmethod
    def read_entity(cls,line):
        """
    Formez o entitate dintr-o linie a fisierului
        """
        line = line.split(sep=',')
        
        id = line[0]
        nume = line[1]
        locatie = line[2]
        capacitate = line[3]
        pret = line[4]
        return House(id,nume,locatie,capacitate,pret)

    @classmethod
    def write_entity(cls,entity):
        """
    Tiparesc entitatea pe o linie a fisierului
        """
        return str( str(entity.get_id()) + ',' + entity.get_nume() + ',' + entity.get_locatie() + ',' + str(entity.get_capacitate() )+ ',' + str(entity.get_pret_noapte()))
    
    def __str__(self):
        """
    Transform entitatea in string pentru a putea fi tiparita
        """
        return str( str(self.get_id()) + ',' + self.get_nume() + ',' + self.get_locatie() + ',' + str(self.get_capacitate() )+ ',' + str(self.get_pret_noapte()))


class InchiriereDTO(object):
#Prin aceasta casa abstractizez o inchiriere         
    def __init__(self, _nume, _locatie, _capacitate, _pret):
        self.__nume = _nume
        self.__locatie = _locatie
        self.__capacitate = _capacitate
        self.__pret = _pret

    def get_nume(self):
        return self.__nume


    def get_locatie(self):
        return self.__locatie


    def get_capacitate(self):
        return self.__capacitate


    def get_pret(self):
        return self.__pret


    def set_nume(self, value):
        self.__nume = value


    def set_locatie(self, value):
        self.__locatie = value


    def set_capacitate(self, value):
        self.__capacitate = value


    def set_pret(self, value):
        self.__pret = value

        
    def __str__(self):
    
        return str(self.get_nume() + ',' + self.get_locatie() + ',' + str(self.get_capacitate() )+ ',' + str(self.get_pret()))

      


