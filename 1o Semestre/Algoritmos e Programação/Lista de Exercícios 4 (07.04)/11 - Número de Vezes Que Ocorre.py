txt = str(input("Escreva qualquer texto: "))
car = str(input("Escolha uma sequência de caracteres presente no texto: "))
qtd = txt.count(car)

print(f'"{car}" ocorre {qtd} vezes no texto')