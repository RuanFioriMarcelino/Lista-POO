from hotel import Simples, Duplo, Suite

simples = Simples(1,"Cricíuma",1,120)
simples.calcularSimples()
simples.disponibilidade("disponivel")
print(simples.__dict__)

duplo = Duplo(2,"Cricíuma",2,120)
duplo.calcularSimples()
duplo.disponibilidade("disponivel")
print(duplo.__dict__)

suite = Suite(4,"Cricíuma",2,120)
suite.calcularSimples()
suite.disponibilidade("disponivel")
print(suite.__dict__)