from gerenciamento import Software, Marketing, Pesquisa


software = Software("Desenvolver uma solução", "sla", "Ruan", "15-04-2024")
marketing = Marketing("Publicar", "teste", "Mari", "05-06-2024")
pesquisa = Pesquisa("Buscar melhorias", "Pegar informações", "Stefany", "27-04-2024")


software.funResponsavel("Belone")
software.defPrazo("20-04-2024")
software.verInformacoes()
software.funConcluir()
software.verProgresso()

""" marketing.funResponsavel("Kaua")
marketing.defPrazo("02-06-2024")
marketing.verInformacoes()
marketing.funConcluir()
marketing.verProgresso()

pesquisa.funResponsavel("Bruno")
pesquisa.defPrazo("20-04-2024")
pesquisa.verInformacoes()
pesquisa.funConcluir()
pesquisa.verProgresso() """