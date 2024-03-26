from funcionarios import Func

funci = Func("Pedro",12345678900,1200)
print(funci.__dict__)
funci.funcCargo()
print(funci.__dict__)
funci.calcularBonus()
print(funci.__dict__)