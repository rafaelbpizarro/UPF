def contar_palavras(arquivo):
    # Dicionário para armazenar as contagens de palavras
    contagem_palavras = {}

    # Abre o arquivo em modo de leitura
    f = open(arquivo, 'r', encoding="UTF-8")

    # Itera sobre cada linha do arquivo
    for linha in f:
        # Divide a linha em palavras
        palavras = linha.split()
        
        # Itera sobre cada palavra na linha
        for palavra in palavras:
            # Remove qualquer pontuação das palavras
            palavra = palavra.strip('\n').lower()
            # Incrementa a contagem da palavra no dicionário
            contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    return contagem_palavras

def main():
    arquivo = input("Digite o caminho do arquivo de texto: ")

    try:
        contagem_palavras_resultado = contar_palavras(arquivo)
        # Exibe a contagem de palavras
        for palavra, contagem in contagem_palavras_resultado.items():
            print(f'{palavra}: {contagem}')
    except FileNotFoundError:
        print("Arquivo não encontrado.")

# programa principal
main()
