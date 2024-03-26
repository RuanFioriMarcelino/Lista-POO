from escola import Aluno, Professor

aluno = Aluno('ruan', 52158, '123Ruan', [6, 7, 8])
print(aluno.__dict__)
aluno.verNotas() 
aluno.alterarSenha('ruan123')
print(aluno.__dict__)

professor = Professor('belone', 55658, '123belone', ['13:15 Sala A', '15:55 Sala B'])
print(professor.__dict__)
professor.verHorarios()
professor.alterarSenha('belone123')
print(professor.__dict__)