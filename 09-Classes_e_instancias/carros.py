class Carros():
    def __init__(self,construtora,modelo,ano):
        self.construtora=construtora
        self.modelo=modelo
        self.ano=ano
        self._odometro=0
    def descricao(self):
        return self.construtora+" - "+self.modelo+" - "+str(self.ano)
    def getOdometro(self):
        return self._odometro
    def setOdometro(self,odometro):
        if(odometro<self._odometro):
            return -1
        else:
            self._odometro=odometro

class CarroEletrico(Carros):
    def __init__(self,fabricante,modelo,ano):
        super().__init__(fabricante,modelo,ano)