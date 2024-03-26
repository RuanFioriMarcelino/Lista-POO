from ecossistemas import Animais, Plantas

animal = Animais(8,10,10,4,2)
print(animal.__dict__)
animal.movimentar(4)
print(animal.__dict__)
animal.comer(6)
print(animal.__dict__)