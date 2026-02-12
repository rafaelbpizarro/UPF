from funcao import EstaOrdenada

entrada = input("Escreva uma lista de números separados por espaço ou vírgula: ")
entrada = entrada.replace(",", " ")
lista = entrada.split()

print(EstaOrdenada(lista))


