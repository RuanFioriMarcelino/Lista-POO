from biblioteca import Livros, Revistas

""" livro = Livros("Diario de fulano", "Eu", 2024,5, 12345)
print(livro.__dict__)
livro.funEmprestimo("Ruan", 12345)
print(livro.__dict__)
livro.funDevolucao()
livro.funDisponibilidade(12345) """

revista = Revistas("Jornal", "UOL", 2024,10, 23451)
print(revista.__dict__)
revista.funEmprestimo("João", 23451)
print(revista.__dict__)
revista.funDevolucao()
revista.funDisponibilidade(23451)