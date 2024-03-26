from redesocial import Padrao, Influenciador, Empresa

""" padrao = Padrao('ruan', 'ruan@gmail.com', 0,0, 'ruan123')
print(padrao.__dict__)
padrao.postar(4)
padrao.curtir()
padrao.rdfSenha('123ruan')
print(padrao.__dict__) """

""" influenciador = Influenciador('joao', 'joao@gmail.com', 0,0,0, 'joao123')
print(influenciador.__dict__)
influenciador.postar(4)
influenciador.curtir()
influenciador.insights()
influenciador.rdfSenha('123joao')
print(influenciador.__dict__) """

empresa = Empresa('pedro', 'pedro@gmail.com', 0,0,0, 'pedro123')
print(empresa.__dict__)
empresa.postar(4)
empresa.curtir()
empresa.insights()
empresa.rdfSenha('123pedro')
empresa.anunciar("Carro")
print(empresa.__dict__)