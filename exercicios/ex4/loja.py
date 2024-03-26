""" Sistema de Estoque para Loja Online:
Desenvolva um sistema de estoque para uma loja online que inclua diferentes tipos de 
produtos, como eletrônicos, vestuário, alimentos, etc. Cada tipo de produto deve ter 
métodos para calcular preço final, descontos, etc. """

class Estoque():
    def __init__(self, descricao, genero, valor):
        self.descricao = descricao
        self.genero = genero
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self):
        raise ValueError ("Valor não pode ser alterado diretamente!")
    
    def valorProduto(self,a):
        self.__valor -= a
        print(f'Valor do produto final R$ {self.__valor}')
    

class Eletronicos(Estoque):
    def __init__(self, descricao, genero, valor):
        super().__init__(descricao, genero, valor)
        
    def calcularDesconto(self,a):
        x = (self.valor * a) / 100
        self.valorProduto(x)

class Vestuario(Estoque):
    def __init__(self, descricao, genero, valor):
        super().__init__(descricao, genero, valor)
        
    def calcularDesconto(self,a):
        x = (self.valor * a) / 100
        self.valorProduto(x)

class Alimentos(Estoque):
    def __init__(self, descricao, genero, valor):
        super().__init__(descricao, genero, valor)
        
    def calcularDesconto(self,a):
        x = (self.valor * a) / 100
        self.valorProduto(x)