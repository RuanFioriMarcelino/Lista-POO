from cinema import Normal,InVIP,In3D

normal = Normal("Normal", 25, 200)
print(normal.__dict__)
vip = InVIP("vip", 50, 100)
print(vip.__dict__)
in3D = In3D("3D", 35, 200 )
print(in3D.__dict__)


print(f'Valor do(s) ingresso(s) R${normal.funPreco(4)}')
print(f'Valor do(s) ingresso(s) R${vip.funPreco(2)}')
print(f'Valor do(s) ingresso(s) R${in3D.funPreco(3)}')