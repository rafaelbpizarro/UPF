negativo = []
positivo = []

for i in range(1, 11):
    numero = int(input(f"Escolha o {i}o número: "))
    if numero < 0:
        negativo.append(numero)
    elif numero > 0:
        positivo.append(numero)
    else:
        print("ERRO")
        exit()

print(f"\nNúmero positivos: {positivo} \nNúmero negativos: {negativo}")