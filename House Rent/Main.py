'''
Created on 13 dec. 2019

@author: Alex
'''
#Teste
from teste.testeRepo import TestRepo
from teste.testeService import TestService

#Repository
from domain.entitati import House
from infrastructure.repository import RepositoryFile
repoHouse = RepositoryFile('./inchirieri.txt', House)

#Service
from business.service import ServiceHouse
serviceHouse = ServiceHouse(repoHouse)

#UI
from prezentare.console import Console
ui = Console(serviceHouse)
ui.run()
