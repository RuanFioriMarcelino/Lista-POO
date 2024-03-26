""" Sistema de Gerenciamento de Escola:
Crie um sistema de gerenciamento para uma escola que inclua diferentes tipos de
usuários, como alunos, professores, funcionários, etc. Cada tipo de usuário deve ter
métodos para acessar notas, horários, comunicados, etc. """

class Escola():
    def __init__(self,nome,codigo,senha):
        self.nome = nome
        self.codigo = codigo
        self.__senha = senha

    @property
    def senha(self):
        return self.__senha

    def rdfSenha(self, a):
        self.__senha = a

class Aluno(Escola):
    def __init__(self, nome, codigo, senha, notas):
        super().__init__(nome, codigo, senha)
        self.notas = notas
    
    def verNotas(self):
        print(f'Aluno possui as seguintes notas: {self.notas}')

    def alterarSenha(self,x):
        a = x
        self.rdfSenha(a)

class Professor(Escola):
    def __init__(self, nome, codigo, senha, horarios):
        super().__init__(nome, codigo, senha)
        self.horarios = horarios

    def verHorarios(self):
        print(f'Seu horario de aula: {self.horarios}')

    def alterarSenha(self,x):
        a = x
        self.rdfSenha(a)