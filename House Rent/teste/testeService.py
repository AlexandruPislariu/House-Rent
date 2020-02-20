from business.service import ServiceHouse
from infrastructure.repository import Repo
from domain.entitati import House

import unittest

class TestService(unittest.TestCase):
#Aici testez functiile din service  
    def setUp(self):
    #Creez cateva locuinte
        self.h1 = House(1,'da','Burdujeni',10,100)
        self.h2 = House(2,'da','Burdujeni',9,100)
        self.h3 = House(3,'da','Burdujeni',8,100)
        self.h4 = House(4,'da','Burdujeni',7,10)
        self.h5 = House(5,'da','Burdujeni',6,100)
        
    #le adaug in repository
        self.repo = Repo()
        self.repo.adauga_entitate(self.h1)
        self.repo.adauga_entitate(self.h2)
        self.repo.adauga_entitate(self.h3)
        self.repo.adauga_entitate(self.h4)
        self.repo.adauga_entitate(self.h5)
        
    #creez service
        self.service = ServiceHouse(self.repo)
        
    def tearDown(self):
        pass
    
    def test_find_houses(self):
        
        exemplu = self.service.find_houses('Burdujeni',8)
        self.assertEqual(exemplu, [self.h1,self.h2,self.h3])

        exemplu = self.service.find_houses('Suceava',8)
        self.assertEqual(exemplu, [])
        
    def test_rent(self):
        
        exemplu = self.service.rent(1,3)
        self.assertEqual(exemplu.get_nume(), self.h1.get_nume())
        self.assertEqual(int(exemplu.get_pret()), 3*int(self.h1.get_pret_noapte()))
        
        exemplu = self.service.rent(4,3)
        self.assertEqual(exemplu.get_nume(), self.h4.get_nume())
        self.assertEqual(int(exemplu.get_pret()), 3*int(self.h4.get_pret_noapte()))
        
if __name__=='__main__':
    unittest.main()