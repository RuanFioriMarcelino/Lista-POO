""" 12. Simulação de Mercado Financeiro: 
Implemente uma simulação de mercado financeiro com diferentes tipos de 
investimentos, como ações, títulos, fundos imobiliários, etc. Cada tipo de investimento 
deve ter métodos para calcular retorno, risco, etc. """

class McFinanceiro():
    def __init__(self,nome, valor):
        self.nome = nome
        self.__valor = valor
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self):
        raise ValueError("Valor não pode ser alterado diretamente! ")

class Acoes(McFinanceiro):
    def __init__(self, nome, valor, preco):
        super().__init__(nome, valor)
        self.preco = preco

    def ganho(self):
        return (self.preco - self.valor) / self.valor

    def risco(self):
        print("Ação de grande risco!")

class Titulos(McFinanceiro):
    def __init__(self, nome, valor, taxa):
        super().__init__(nome, valor)
        self.taxa = taxa

    def ganho(self):
        return self.valor * self.taxa

    def risco(self):
        print("Titulo de baixo risco!")


class Imobiliario(McFinanceiro):
    def __init__(self, nome, valor, renda):
        super().__init__(nome, valor)
        self.renda = renda

    def ganho(self):
        return self.renda * 12 / self.valor

    def risco(self):
        print("Fundo de médio risco!")
