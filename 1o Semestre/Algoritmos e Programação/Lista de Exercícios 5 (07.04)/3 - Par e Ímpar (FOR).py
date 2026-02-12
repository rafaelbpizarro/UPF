num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    num1, num2 = num2, num1

pares = []
impares = []


for i in range(num1 + 1, num2):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)


print(f"Números pares entre os dois valores: {pares}")
print(f"Números ímpares entre os dois valores: {impares}")