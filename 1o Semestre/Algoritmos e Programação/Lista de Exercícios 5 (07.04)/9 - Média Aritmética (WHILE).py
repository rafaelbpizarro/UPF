soma = 0
quantidade = 0

print("Digite números para calcular a média.")
print("Digite 0 para encerrar a entrada de dados.\n")

while True:
    numero = float(input("Digite um número (0 para parar): "))

    if numero == 0:
        break  

    soma += numero           
    quantidade += 1          

if quantidade > 0:
    media = soma / quantidade
    print("\nQuantidade de números informados:", quantidade)
    print("Média aritmética:", media)
else:
    print("\nNenhum número válido foi informado.")