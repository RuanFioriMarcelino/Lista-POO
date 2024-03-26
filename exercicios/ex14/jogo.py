""" Jogo de Estratégia em Tempo Real (RTS):
Desenvolva um jogo de estratégia em tempo real que permita controlar diferentes tipos
de unidades, como soldados, tanques, aeronaves, etc. Cada tipo de unidade deve ter
métodos para atacar, mover-se, defender, etc. """

class Jogo:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.__vida = vida
        self.ataque = ataque
        self.defesa = defesa

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self):
        raise ValueError("Valor não pode ser alterado diretamente! ")

    def funMover(self, a):
        print(f'{self.nome} foi para { a }.')

    def funAtacar(self, i):
        print(f'{self.nome} atacou {i.nome }. ')

    def funDefender(self):
        print(f'{self.nome} ta na defensiva.')


class Inimigo(Jogo):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
class Soldado(Jogo):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
class Tanque(Jogo):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
class Aeronave(Jogo):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)


