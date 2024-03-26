""" Sistema de Gestão de Biblioteca:
Desenvolva um sistema de gestão para uma biblioteca que inclua diferentes tipos de
materiais, como livros, revistas, CDs, etc. Cada tipo de material deve ter métodos para
empréstimo, devolução, consulta de disponibilidade, etc """

class Biblioteca():
    def __init__(self, nome, autor, ano, quantidade, codigo):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.quantidade = quantidade
        self.emprestimo = 0
        self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self):
        raise ValueError("Valor não pode ser alterado diretamente! ")
    
class Livros(Biblioteca):
    def __init__(self, nome, autor, ano, quantidade, codigo):
        super().__init__(nome, autor, ano, quantidade, codigo)

    def funEmprestimo(self, nome, cod):
        if cod == self.codigo:
            if self.quantidade > 1:
                self.emprestimo += 1
                self.quantidade -= 1
                print(f'Livro de código {self.codigo} emprestado para {nome}')

    def funDevolucao(self):
        self.emprestimo -= 1
        self.quantidade += 1
        print(f"Livro {self.nome} devolvido! ")
    
    def funDisponibilidade(self,cod):
        if self.quantidade > 0 and cod == self.codigo:
            print("Livro ainda disponível")
        else:
            print("Livro indisponível")

class Revistas(Biblioteca):
    def __init__(self, nome, autor, ano, quantidade, codigo):
        super().__init__(nome, autor, ano, quantidade, codigo)

    def funEmprestimo(self, nome, cod):
        if cod == self.codigo:
            if self.quantidade > 1:
                self.emprestimo += 1
                self.quantidade -= 1
                print(f'Revista de código {self.codigo} emprestado para {nome}')

    def funDevolucao(self):
        self.emprestimo -= 1
        self.quantidade += 1
        print(f"Revista {self.nome} devolvido! ")
    
    def funDisponibilidade(self,cod):
        if self.quantidade > 0 and cod == self.codigo:
            print("Revista ainda disponível")
        else:
            print("Revista indisponível")