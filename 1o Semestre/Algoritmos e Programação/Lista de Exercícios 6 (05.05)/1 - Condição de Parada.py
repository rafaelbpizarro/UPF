numeros = []
repetidos = []

print("Digite números para adicionar a lista.")
print("Digite 0 para encerrar a entrada de dados.\n")

while True:
    numero = int(input("Digite um número (0 para parar): "))

    if numero == 0:
        break
    elif numero > 0:
        if numero not in numeros:
            numeros.append(numero)
        else:
            numeros.append(numero)
            numeros.remove(numero)

numeros.sort()
print(f"Os números escolhidos foram: {numeros}")