""" Rede Social com Perfis de Usuários:
Desenvolva uma rede social que permita criar diferentes tipos de perfis de usuários,
como padrão, influenciador, empresa, etc. Cada tipo de perfil deve ter métodos para
postar conteúdo, interagir com outros usuários, etc. """

class RedeSocial():
    def __init__(self,nome,login,post,curtida,visualizacao,senha):
        self.nome = nome
        self.login = login
        self.post = post
        self.curtida = curtida
        self.visualizacao = visualizacao
        self.__senha = senha

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self):
        raise ValueError("Valor não pode ser alterado diretamente! ")
    
    def redefinirSenha(self, a):
        self.__senha = a

    
class Padrao(RedeSocial):
    def __init__(self, nome, login, post, curtida, visualizacao, senha):
        super().__init__(nome, login, post, curtida, visualizacao, senha)
    
    def postar(self, a):
        self.post += a
    
    def curtir(self):
        self.curtida += 1
        print(self.curtida," post(s) curtido(s)!")


    def rdfSenha(self, x):
        a = x
        self.redefinirSenha(a)

class Influenciador(RedeSocial):
    def __init__(self, nome, login, post, curtida, visualizacao, senha):
        super().__init__(nome, login, post, curtida, visualizacao, senha)
    
    def postar(self, a):
        self.post += a
    
    def curtir(self):
        self.curtida += 1
        print(self.curtida," post(s) curtido(s)!")

    def insights(self):
        print(f'{self.curtida} curtida(s) no seu post e {self.visualizacao} visualizações.')

    def rdfSenha(self, x):
        a = x
        self.redefinirSenha(a)

class Empresa(RedeSocial):
    def __init__(self, nome, login, post, curtida, visualizacao, senha):
        super().__init__(nome, login, post, curtida, visualizacao, senha)
    
    def postar(self, a):
        self.post += a
    
    def curtir(self):
        self.curtida += 1
        print(self.curtida," post(s) curtido(s)!")

    def insights(self):
        print(f'{self.curtida} curtida(s) no seu post e {self.visualizacao} visualizações.')
    
    def anunciar(self,a):
        print(f"{a} anunciado nas principais páginas!")

    def rdfSenha(self, x):
        a = x
        self.redefinirSenha(a)