from reservasAereas import Economico,Executivo,PrimeiraClasse

eco = Economico("Gol",12,"16-03-2024", "Forquilhinha", "Criciuma")
exe = Executivo("Qatar",32,"21-04-2025","Brasil","China")
pri = PrimeiraClasse("Qatar",35,"11-04-2024","China","Brasil")

eco.calcularDisp("Ruan")
print(eco.__dict__)
exe.calcularDisp("Luan")
print(exe.__dict__)
pri.calcularDisp("Bruno")
print(pri.__dict__)