txt = str(input("Escreva qualquer texto: "))
posicao = int(input("Qual o número do caracter (de trás para frente)? "))
caracter = (txt[posicao * -1])

print(f'O caracter é "{caracter}"')