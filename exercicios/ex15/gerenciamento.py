"""  Sistema de Gerenciamento de Projeto:
Crie um sistema de gerenciamento de projeto que inclua diferentes tipos de tarefas,
como desenvolvimento de software, marketing, pesquisa, etc. Cada tipo de tarefa deve
ter métodos para atribuir responsáveis, definir prazos, monitorar progresso, etc. """

class Tarefa:
    def __init__(self, nome, descricao, responsavel, prazo):
        self.nome = nome
        self.descricao = descricao
        self.responsavel = responsavel
        self.prazo = prazo
        self.concluida = "Não concluido"

    def funResponsavel(self, responsavel):
        self.responsavel = responsavel

    def defPrazo(self, prazo):
        self.prazo = prazo

    def funConcluir(self):
        self.concluida = "Concluído"

    def verProgresso(self):
        if self.concluida == "Concluído":
            print(f"Tarefa {self.nome} concluída.")
        else:
            print(f"Tarefa {self.nome} não concluída.")


class Software(Tarefa):
    def __init__(self, nome, descricao, responsavel, prazo):
        super().__init__(nome, descricao, responsavel, prazo)

    def verInformacoes(self):
        print(f'Responsavel pelo projeto: {self.responsavel}\nNome do projeto: {self.nome}\nPrazo de entrega {self.prazo}')

class Marketing(Tarefa):
    def __init__(self, nome, descricao, responsavel, prazo):
        super().__init__(nome, descricao, responsavel, prazo)

    def verInformacoes(self):
        print(f'Responsavel pelo projeto: {self.responsavel}\nNome do projeto: {self.nome}\nPrazo de entrega {self.prazo}')

class Pesquisa(Tarefa):
    def __init__(self, nome, descricao, responsavel, prazo):
        super().__init__(nome, descricao, responsavel, prazo)

    def verInformacoes(self):
        print(f'Responsavel pelo projeto: {self.responsavel}\nNome do projeto: {self.nome}\nPrazo de entrega {self.prazo}')