""" Sistema de Registro de Funcionários:
Crie um sistema de registro de funcionários que permita adicionar funcionários de
diferentes tipos (por exemplo, gerentes, programadores, analistas) com métodos para
calcular salário, bônus, etc. Utilize herança e encapsulamento para organizar a
estrutura """

class Funcionarios():
    def __init__(self,nome,cpf,salario):
        self.nome = nome
        self.cpf = cpf
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self):
        raise ValueError("Salário não pode ser alterado!")
    
    def funcSalario(self,a):
        self.__salario += a
        print("Salário do funcionário é de R$",self.__salario)

class Func(Funcionarios):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def funcCargo(self):
        self.cargo = int(input("1 - Gerente\n2 - Programador\n3 - Analista\n"))
        print(self.cargo)

    def calcularBonus(self):
        if self.cargo == 1:
           self.funcSalario(300)
        elif self.cargo == 2:
            self.funcSalario(200)
        elif self.cargo == 3:
            self.funcSalario(100)