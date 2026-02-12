vogais = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
consoantes = []

entrada = input(f"Escreva uma lista com 10 caracteres (separados por espaço): ")
lista = entrada.split()

if len(lista) != 10:
    print("A lista deve ter 10 caracteres.")
else:
    for char in lista:
        if char not in vogais:
            consoantes.append(char)

if len(consoantes) != 0:
    print(f"{len(consoantes)} consoantes foram lidas, elas são:\n{consoantes}")
else:
    print("A lista não possui consoantes")