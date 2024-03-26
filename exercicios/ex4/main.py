from loja import Eletronicos

eletronicos = Eletronicos('Geladeira','eletrodomestico',2000)
print(eletronicos.__dict__)
eletronicos.calcularDesconto(5)
print(eletronicos.__dict__)
