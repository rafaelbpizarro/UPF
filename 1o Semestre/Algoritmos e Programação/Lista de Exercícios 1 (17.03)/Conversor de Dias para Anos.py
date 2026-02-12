print("Conversor de dias para anos")
Dias = int(input("Número de Dias: "))
Anos = Dias // 365
DiasRest = Dias % 365
Meses = DiasRest // 30
DiasRest2 = DiasRest % 30
print(Dias, "dias equivalem a ", Anos, "ano(s) ", Meses, "mês(es) e ", DiasRest2, "dia(s)")