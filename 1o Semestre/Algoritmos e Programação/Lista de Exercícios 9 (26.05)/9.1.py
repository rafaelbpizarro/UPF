def contar_letras(frase):
    contagem = {}
    # percorre todas as posicoes das string
    for letra in frase:
        # testa se o caractere e valido
        if letra.isalpha():
            letra = letra.upper()
            # testa de letra ja esta sendo contada
            if letra in contagem :
                contagem[letra] += 1
            else :
                contagem[letra] = 1
    return contagem

frase_entrada = input("Digite uma frase para contar as letras: ")
resultado_contagem = contar_letras(frase_entrada)
print("Contagem de letras:")
for letra, quantidade in resultado_contagem.items():
    print(f"{letra}: {quantidade}")
print("Como esta armazenado: ", resultado_contagem)

