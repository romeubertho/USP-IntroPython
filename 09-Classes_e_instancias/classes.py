'''
NAO EXISTE attr privado em python!
por convencao utiliza "_" para denotar que o attr nao deve ser modificado
ex:
self._attr
'''
from carros import *

class Cachorro():
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    def sentar(self):
        print(self.nome.title()+" esta sentando.")
    def rolar(self):
        print(self.nome.title()+" esta rolando.")
cachorro = Cachorro("Astor",5)
cachorro.sentar()

class Carro():
    def __init__(self,construtora,modelo,ano):
        self.construtora=construtora
        self.modelo=modelo
        self.ano=ano
        self.odometro=0
    def descricao(self):
        return self.construtora+" - "+self.modelo+" - "+str(self.ano)
    def getOdometro(self):
        return self.odometro
    def setOdometro(self,odometro):
        self.odometro=odometro
carro = Carro("A","B", 95)
print(str(carro.descricao()))
print(str(carro.getOdometro()))
carro.setOdometro(100)
print(str(carro.getOdometro()))

print("-----")

carro2=Carros("B","C",2015)
print(str(carro2.descricao()))
print(str(carro2.getOdometro()))
carro2.setOdometro(100)
print(str(carro2.getOdometro()))
carro2.setOdometro(50)
print(str(carro2.getOdometro()))

tesla = CarroEletrico("tesla","model s",2017)
print(str(tesla.descricao()))