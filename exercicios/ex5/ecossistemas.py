""" Simulação de Ecossistema com Seres Vivos:
Implemente uma simulação de um ecossistema com diferentes tipos de seres vivos,
como animais, plantas, etc. Cada tipo de ser vivo deve ter comportamentos específicos,
como movimento, alimentação, reprodução, etc. """

class Ecossistema ():
    def __init__(self,saude, estamina, alimentacao, crescimento, reproducao): #escala de 0 a 10
        self.__saude = saude
        self.estamina = estamina
        self.alimentacao = alimentacao
        self.crescimento = crescimento
        self.reproducao = reproducao
    
    @property
    def saude(self):
        return self.__saude
    
    @saude.setter
    def saude(self):
        raise ValueError("Valor não pode ser alterado diretamente! ")
    
    def aumSaude(self, a):
        self.__saude += a
    
class Animais(Ecossistema):
    def __init__(self, saude, estamina, alimentacao, crescimento, reproducao):
        super().__init__(saude, estamina, alimentacao, crescimento, reproducao)

    def movimentar(self,a):
        self.estamina -= a
        self.alimentacao -= a
        x = a / 2
        self.aumSaude(x)
    
    def comer(self,a):
        self.crescimento += a / 2
        self.alimentacao += a
        self.estamina += a / 2
        x = a / 2
        self.aumSaude(x)

class Plantas(Ecossistema):
    def __init__(self, saude, estamina, alimentacao, crescimento, reproducao):
        super().__init__(saude, estamina, alimentacao, crescimento, reproducao)

    def movimentar(self,a):
        self.alimentacao -= a
        x = a / 2
        self.aumSaude(x)
    
    def comer(self,a):
        self.crescimento += a / 2
        self.alimentacao += a
        x = a / 2
        self.aumSaude(x)