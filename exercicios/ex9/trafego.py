""" Simulação de Tráfego em uma Cidade:
Implemente uma simulação de tráfego em uma cidade com diferentes tipos de veículos,
como carros, ônibus, bicicletas, etc. Cada tipo de veículo deve ter métodos para calcular
rotas, tempo de viagem, etc.
 """

class Trafego():
    def __init__(self,marca,modelo,cor,ano,chassi):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor 
        self.ano = ano
        self.__chassi = chassi

    @property
    def chassi(self):
        return self.__chassi

    @chassi.setter
    def chassi(self):
        raise ValueError("Valor não pode ser alterado diretamente! ")
    
    def alterarChassi(self, a):
        self.__chassi = a

class Carros(Trafego):
    def __init__(self, marca, modelo, cor, ano, chassi, velocidade):
        super().__init__(marca, modelo, cor, ano, chassi)
        self.velocidade = velocidade 

    def calcularTempoRota(self, distancia):
        tmpPercorrido = distancia / self.velocidade
        print(f'Tempo para chegar no destino estimado em {tmpPercorrido} Horas em uma velocidade de {self.velocidade} Km/h')
    
    def altChassi(self):
        chassi = input("Digite o chassis do carro: ")
        self.alterarChassi(chassi)

class Onibus(Trafego):
    def __init__(self, marca, modelo, cor, ano, chassi, velocidade, passageiros, ganhoDia):
        super().__init__(marca, modelo, cor, ano, chassi)
        self.velocidade = velocidade 
        self.passageiros = passageiros
        self.valorPassagem = 5.16
        self.ganhoDia = ganhoDia

    def calcularTempoRota(self, distancia):
        tmpPercorrido = distancia / self.velocidade
        print(f'Tempo para chegar no destino estimado em {tmpPercorrido} Horas em uma velocidade de {self.velocidade} Km/h')

    def altChassi(self):
        chassi = input("Digite o chassis do carro: ")
        self.alterarChassi(chassi)

    def passageiro(self):
        p = int(input("Quantos passageiros subiram: "))
        self.passageiros += p

    def calcularValor(self):
        self.ganhoDia = self.valorPassagem * self.passageiros
        print(f"Trasportados {self.passageiros} passageiros, ganho no total de {self.ganhoDia}")