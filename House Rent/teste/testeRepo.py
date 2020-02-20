from infrastructure.repository import Repo
from domain.entitati import House

import unittest
from exceptii.erori import RepoError
class TestRepo(unittest.TestCase):
#Aici testez functiile din repository   
    def setUp(self):
    #creez cateva locuinte 
        self.h1 = House(1,'da','Burdujeni',10,100)
        self.h2 = House(2,'da','Burdujeni',10,100)
        self.h3 = House(3,'da','Burdujeni',10,100)
        self.h4 = House(4,'da','Burdujeni',10,100)
        self.h5 = House(5,'da','Burdujeni',10,100)
        
    #le adaug in repository
        self.repo = Repo()
        self.repo.adauga_entitate(self.h1)
        self.repo.adauga_entitate(self.h2)
        self.repo.adauga_entitate(self.h3)
        self.repo.adauga_entitate(self.h4)
        self.repo.adauga_entitate(self.h5)
        
    def tearDown(self):
        pass
    
    def test_get_all(self):
        
        self.assertEqual(self.repo.get_all(), [self.h1,self.h2,self.h3,self.h4,self.h5])
        
    def test_adauga_entitate(self):
        
        h6 = House(1,'da','Burdujeni',10,100)
        
        with self.assertRaises(RepoError):
            self.repo.adauga_entitate(h6)
            
        h7 = House(6,'da','Burdujeni',10,100)
        self.assertEqual(self.repo.adauga_entitate(h7), [self.h1,self.h2,self.h3,self.h4,self.h5,h7])

    def test_cauta_entitate(self):
        
        self.assertEqual(self.repo.cauta_entitate(self.h1), 0)
        self.assertEqual(self.repo.cauta_entitate(self.h5), 4)
        self.assertEqual(self.repo.cauta_entitate(self.h3), 2)
        h6 = House(10,'da','Burdujeni',10,100)
        self.assertEqual(self.repo.cauta_entitate(h6), -1)
        
    def test_get_entitate(self):
        
        exemplu = self.repo.get_entitate(0)
        self.assertEqual(exemplu.get_id(), self.h1.get_id())
        
        exemplu = self.repo.get_entitate(4)
        self.assertEqual(exemplu.get_id(), self.h5.get_id())
        
        
if __name__=='__main__':
    unittest.main()