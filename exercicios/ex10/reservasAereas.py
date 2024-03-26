""" Sistema de Reservas para Companhia Aérea:
Desenvolva um sistema de reservas para uma companhia aérea que permita reservar
diferentes tipos de voos, como econômico, executivo, primeira classe, etc. Cada """

class Reservas():
    def __init__(self,companhia, assento, data, origem, destino):
        self.companhia = companhia
        self.assento = assento
        self.data = data
        self.origem = origem
        self.destino = destino
        self.quantidade = 100
        self.reservados = 0

    def calcularDisp(self,a):
        if self.quantidade > self.reservados:
            print(f"Reserva feita para {a}, voo de {self.origem} ate {self.destino}.")
            self.reservados =+1
        else:
            print("Reserva não aprovada")
    
class Economico(Reservas):
    def __init__(self, companhia, assento, data, origem, destino):
        super().__init__(companhia, assento, data, origem, destino)
        self.valorPassagem = 100    
    
    def funVoos(self):
        return self.valorPassagem
    
class Executivo(Reservas):
    def __init__(self, companhia, assento, data, origem, destino):
        super().__init__(companhia, assento, data, origem, destino)
        self.valorPassagem = 100    
    
    def funVoos(self):
        return self.valorPassagem * 2
    

class PrimeiraClasse(Reservas):
    def __init__(self, companhia, assento, data, origem, destino):
        super().__init__(companhia, assento, data, origem, destino)
        self.valorPassagem = 100    
    
    def funVoos(self):
        return self.valorPassagem * 3