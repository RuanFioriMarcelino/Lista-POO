""" Sistema de Reservas para Cinema:
Crie um sistema de reservas para um cinema que permita reservar diferentes tipos de
ingressos, como normal, VIP, 3D, etc. Cada tipo de ingresso deve ter métodos para
calcular preço, disponibilidade, etc. """

class Cinema():
    def __init__(self, tipo, preco, disponibilidade):
        self.tipo = tipo
        self.__preco = preco
        self.disponibilidade = disponibilidade

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self):
        raise ValueError("Valor não pode ser alterado diretamente")

    def funPreco(self, q):
        print(f"{q} assentos comprados, disponiveis: {self.disponibilidade-q}")
        return self.preco * q

    def funDisponibilidade(self, q):
        return self.disponibilidade >= q
    
class Normal(Cinema):
    def __init__(self, tipo, preco, disponibilidade):
        super().__init__(tipo, preco, disponibilidade)

class InVIP(Cinema):
    def __init__(self, tipo, preco, disponibilidade):
        super().__init__(tipo, preco, disponibilidade)

class In3D(Cinema):
    def __init__(self, tipo, preco, disponibilidade):
        super().__init__(tipo, preco, disponibilidade)