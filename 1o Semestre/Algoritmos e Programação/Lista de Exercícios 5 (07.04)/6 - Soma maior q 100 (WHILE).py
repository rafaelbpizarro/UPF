soma = 0
quantidade = 0
numeros = []

while soma <= 100:
    numero = int(input("Digite um número: "))
    soma += numero                        
    quantidade += 1
    numeros.append(numero)

print(f"\nQuantidade de números lidos até a soma ultrapassar 100: {quantidade} \nNúmeros: {numeros} \nSoma: {soma}")