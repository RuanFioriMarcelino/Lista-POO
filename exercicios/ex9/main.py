from trafego import Carros, Onibus

""" carro = Carros('Chevrolet','Vectra','Preto',2012,'4D94JNS2',100)
print(carro.__dict__)
carro.calcularTempoRota(120)
carro.altChassi()
print(carro.__dict__) """

onibus = Onibus('Mercedes','TORINO','Branco',2011,'4D94JNS2', 60, 0 ,0)
print(onibus.__dict__)
onibus.calcularTempoRota(120)
onibus.altChassi()
onibus.passageiro()
onibus.calcularValor()
print(onibus.__dict__)