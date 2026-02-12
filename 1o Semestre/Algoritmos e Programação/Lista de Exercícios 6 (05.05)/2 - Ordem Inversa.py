entrada = input("Escreva uma lista de 10 números separados por espaço ou vírgula: ")
entrada = entrada.replace(",", " ")
lista = entrada.split()

if len(lista) != 10:
    print("A lista deve ter 10 números.")

else:
    lista = [int(numero) for numero in lista]
    lista.reverse()
    print(f"\nNúmeros lidos na ordem inversa:\n{lista}")