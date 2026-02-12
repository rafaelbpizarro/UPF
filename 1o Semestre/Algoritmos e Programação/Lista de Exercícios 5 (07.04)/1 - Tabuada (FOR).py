numero = int(input("Digite um número para ver a tabuada: "))

for multiplicacao in range(1, 11):
    resultado = numero * multiplicacao
    print(f"{numero} x {multiplicacao} = {resultado}")