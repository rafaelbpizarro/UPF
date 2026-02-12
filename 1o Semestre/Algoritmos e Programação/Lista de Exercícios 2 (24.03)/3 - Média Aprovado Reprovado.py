print("CALCULE A MÉDIA DE SUAS NOTAS")
Nota1 = float(input("Qual sua primeira nota? "))
Nota2 = float(input("Qual sua segunda nota? "))
Nota3 = float(input("Qual sua terceira nota? "))

if Nota1 < 0 or Nota1 > 10:
    print(f"Erro: nota {Nota1} inválida")
    exit()
if Nota2 < 0 or Nota2 > 10:
    print(f"Erro: nota {Nota2} inválida")
    exit()
if Nota3 < 0 or Nota3 > 10:
    print(f"Erro: nota {Nota3} inválida")
    exit()

Media = (Nota1 + Nota2 + Nota3) / 3
print(f"A sua Média é: {Media:.1f}")
if Media >= 7:
    print("APROVADO")
elif Media < 7:
    print("REPROVADO")