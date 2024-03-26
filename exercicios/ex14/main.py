from jogo import Soldado, Tanque, Aeronave, Inimigo

soldado = Soldado("Bruno",100,30,20)
tanque = Tanque("Luan",200,100,90)
aeronave = Aeronave("Kaua",150,60,40)
inimigo = Inimigo("Belone",300,150,100)


soldado.funMover("a SATC")
soldado.funAtacar(inimigo)
soldado.funDefender()

tanque.funMover("o CC")
tanque.funAtacar(inimigo)
tanque.funDefender()

aeronave.funMover("Enfermaria")
aeronave.funAtacar(inimigo)
aeronave.funDefender()
