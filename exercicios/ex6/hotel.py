"""  Sistema de Reservas para Hotel: 
Crie um sistema de reservas para um hotel que permita reservar diferentes tipos de 
quartos, como simples, duplo, suíte, etc. Cada tipo de quarto deve ter métodos para 
calcular preço da estadia, disponibilidade, etc. """

class Hotel():
    def __init__(self,dias,localizacao,qtdPessoas,valor):
        self.dias = dias
        self.qtdPessoas = qtdPessoas
        self.localizacao = localizacao
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self):
        raise ValueError("O valor não pode ser alterado diretamente! ")

    def calcularQuarto(self):
        x = self.qtdPessoas * (self.dias * self.__valor)
        self.__valor = x
    
class Simples(Hotel):
    def __init__(self, dias, localizacao, qtdPessoas, valor):
        super().__init__(dias, localizacao, qtdPessoas, valor)
    
    def calcularSimples(self):
        self.calcularQuarto()
    
    def disponibilidade(self,a):
        if a.upper() == "DISPONIVEL":
            print("Quarto Disponível.")

        elif a.upper() == "INDISPONIVEL":
            print("Quarto indisponível!")
        else:
            print("Comando não reconhecido!")

class Duplo(Hotel):
    def __init__(self, dias, localizacao, qtdPessoas, valor):
        super().__init__(dias, localizacao, qtdPessoas, valor)
    
    def calcularSimples(self):
        self.calcularQuarto()
    
    def disponibilidade(self,a):
        if a.upper() == "DISPONIVEL":
            print("Quarto Disponível.")

        elif a.upper() == "INDISPONIVEL":
            print("Quarto indisponível!")
        else:
            print("Comando não reconhecido!")

class Suite(Hotel):
    def __init__(self, dias, localizacao, qtdPessoas, valor):
        super().__init__(dias, localizacao, qtdPessoas, valor)
    
    def calcularSimples(self):
        self.calcularQuarto()
    
    def disponibilidade(self,a):
        if a.upper() == "DISPONIVEL":
            print("Quarto Disponível.")

        elif a.upper() == "INDISPONIVEL":
            print("Quarto indisponível!")
        else:
            print("Comando não reconhecido!")