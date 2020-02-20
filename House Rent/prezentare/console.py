from exceptii.erori import ValidError,RepoError
class Console(object):
#UI   
    def __init__(self, serviceHouse):
        self.__serviceHouse = serviceHouse
        self.__panou_comenzi()
        self.__dictionar_comenzi = {'find_houses':self.__ui_find_houses,'rent':self.__ui_rent}
        
    def __panou_comenzi(self):
        """
    Tiparesc utilizatorului functionalitatile disponbile
        """
        print("Comenzile disponibile sunt: \n")
        print("    Cautare locuinte locatie: find_houses \n")
        print("    Inchiriere pe un numar de zile: rent\n")
        print("    Inchiderea aplicatiei: exit \n")
      
    def __ui_find_houses(self,parametrii): 
        """
    Comunica cu utilizatorul pentru a afisa locuintele disponibile cerintei
        """
        
        if len(parametrii)!=2: #locatie,numar persoane
            raise ValueError("Numar incorect de date introduse! ")
        
        locatie = parametrii[0]
        numar_persoare = parametrii[1]
        
        rezultat = self.__serviceHouse.find_houses(locatie,numar_persoare)
        
        for el in rezultat:
            print(el)
            
    def __ui_rent(self,parametrii):
        """
    Comunica cu utilizatorul pentru a inchiria o locuinta pe un anumit numar de zile
        """
        
        if len(parametrii)!=2: #id,numar de zile
            raise ValueError("Numar incorect de date introduse!")
        
        id = parametrii[0]
        numar_zile = parametrii[1]
        
        inchiriere = self.__serviceHouse.rent(id,numar_zile)
        
        print(inchiriere)
        
    def run(self):
        """
    Functie prin care preiau comenzile utilizatorului
        """
        
        while True:
            cmd = input("Introduceti comanda dorita! ")
            
        #Elimin spatiile puse in plus"
            cmd = cmd.strip()
            cmd = cmd.split(sep=';')
            
        #Despart comanda
            nume_comanda = cmd[0]
            parametrii = cmd[1:]
            
            if nume_comanda == 'exit':
                break;
            else:
            #Caut comanda in dictionar
                if nume_comanda in self.__dictionar_comenzi.keys():
                    try:
                        self.__dictionar_comenzi[nume_comanda](parametrii)
                    except ValueError as ve:
                        print("Value Error: \n" + str(ve))
                    except ValidError as vale:
                        print("Valid Error: \n" + str(vale))
                    except RepoError as re:
                        print("Repo Error: \n" + str(re))
                else:
                    print("Comanda invalida!")
                    
                    
    



