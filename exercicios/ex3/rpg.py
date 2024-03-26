""" jogo de RPG com Personagens e Classes:
Crie um jogo de RPG que permita a criação de diferentes tipos de personagens, como 
guerreiros, magos, arqueiros, etc. Cada classe deve ter atributos e métodos específicos, 
como ataque especial, defesa, etc.
 """

class Personagem():
    def __init__(self,forca,velocidade,defesa,vida):
        self.forca = forca
        self.velocidade = velocidade
        self.defesa = defesa
        self.__vida = vida

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self):
        raise ValueError("Valor não pode ser alterado diretamente")
    
    def funVida(self,a):
        self.__vida -= a
        print(f'{self.__vida} de vida')


class Guerreiros(Personagem):
    def __init__(self, forca, velocidade, defesa, vida):
        super().__init__(forca, velocidade, defesa, vida)

    def ataque(self):
        print(f'Ataque de {self.forca}')

    def funDefesa(self):
        print(f'Defesa de {self.defesa}')

class Magos(Personagem):
    def __init__(self, forca, velocidade, defesa, vida):
        super().__init__(forca, velocidade, defesa, vida)

    def ataque(self):
        print(f'Ataque de {self.forca}')

    def funDefesa(self):
        print(f'Defesa de {self.defesa}')
    

class Arqueiros(Personagem):
    def __init__(self, forca, velocidade, defesa, vida):
        super().__init__(forca, velocidade, defesa, vida)

    def ataque(self):
        print(f'Ataque de {self.forca}')

    def funDefesa(self):
        print(f'Defesa de {self.defesa}')
