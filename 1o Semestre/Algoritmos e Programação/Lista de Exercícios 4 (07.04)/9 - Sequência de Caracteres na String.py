txt = str(input("Escreva qualquer texto: "))
car = str(input("Qual sequência de caracteres você quer checar se está no texto? "))

if car in b:
  print(f"{car} faz parte do texto")
if car not in b:
  print(f"{car} não faz parte do texto")