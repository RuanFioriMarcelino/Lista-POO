from mercado import Acoes, Titulos, Imobiliario

acao = Acoes("Vale", 1000, 1200)
titulo = Titulos("CDB", 2500, 0.03)
imobiliario = Imobiliario("SLA", 12000, 1520)

print(acao.__dict__)
print(f'Ganho de {acao.ganho()}')
acao.risco()


print(titulo.__dict__)
print(f'Ganho de {titulo.ganho()}')
titulo.risco()


print(imobiliario.__dict__)
print(f'Ganho de {imobiliario.ganho()}')
imobiliario.risco()
