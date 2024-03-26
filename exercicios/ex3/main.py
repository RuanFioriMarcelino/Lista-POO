from rpg import Guerreiros, Magos, Arqueiros

guerreiro = Guerreiros(10, 7, 8, 6)
print(guerreiro.__dict__)
guerreiro.ataque()
guerreiro.funDefesa()
guerreiro.funVida(3)

""" magos = Magos(6, 10, 9, 10)
print(magos.__dict__)
magos.ataque()
magos.funDefesa()

arqueiros = Arqueiros(8, 10, 10, 7)
print(arqueiros.__dict__)
arqueiros.ataque()
arqueiros.funDefesa() """