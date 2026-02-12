numeros = 0

while numeros < 10:
    numero = int(input(f"Digite o {numeros + 1}º número: "))
    
    if numero == 0:
        print("ERRO: Zero não é positivo nem negativo, escolha outro número")
    else:
        if numero > 0:
            print(f"O número {numero} é Positivo")
        elif numero < 0:
            print(f"O número {numero} é Negativo")
        numeros += 1