valor1 = int(input("Primeiro Valor: "))
valor2 = int(input("Segundo Valor: "))

if valor1 % valor2 == 0 or valor2 % valor1 == 0:
    print(f"Os valores {valor1} e {valor2} são múltiplos")
else:
    print(f"Os valores {valor1} e {valor2} não são múltiplos")