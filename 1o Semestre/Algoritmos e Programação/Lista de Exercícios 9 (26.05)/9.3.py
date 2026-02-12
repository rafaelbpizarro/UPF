import json 

# variaveis globais
dicionario = dict()

def ler(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    
def gravar(nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dicionario, arquivo, indent=4)

def incluir_palavra(palavra, traducao):
    # Inclui uma nova palavra e sua tradução no dicionário
    if palavra in dicionario:
        return(f"\nA palavra '{palavra}' já existe no dicionário.")
    else:
        dicionario[palavra] = traducao
        return(f"\nA palavra '{palavra}' com tradução '{traducao}' foi incluída no dicionário.")

def listar_palavras():
    # Lista todas as palavras do dicionário e suas traduções
    if not dicionario:
        return("\nO dicionário está vazio.")
    else:
        palavras = "\n"
        for palavra, traducao in dicionario.items():
            palavras += f"{palavra}: {traducao} \n"
        return palavras

def alterar_traducao(palavra, nova_traducao):
    # Altera a tradução de uma palavra existente no dicionário
    if palavra in dicionario:
        dicionario[palavra] = nova_traducao
        return(f"\nA tradução da palavra '{palavra}' foi alterada para '{nova_traducao}'.")
    else:
        return(f"\nA palavra '{palavra}' não existe no dicionário.")

def remover_palavra(palavra):
    # Remove uma palavra do dicionário
    if palavra in dicionario:
        dicionario.pop(palavra)
        return(f"\nA palavra '{palavra}' foi removida do dicionário.")
    else:
        return(f"\nA palavra '{palavra}' não existe no dicionário.")

def traduzir(palavra):
    # Retorna a tradução associada com uma palavra
    return dicionario.get(palavra, f"\nA palavra '{palavra}' não existe no dicionário.")

# funcao principal
def main() :
    global dicionario # permite acesso à variavel global
    dicionario = ler("dicionario.json") # busca dados no arquivo json
    
    # print(type(dicionario))
    menu = "\nDicionario\n1.Incluir\n2.Alterar\n3.Excluir\n4.Traduzir\n5.Listar\n9.Sair"
    
    while True :
        print(menu)
        try :
            opcao = int(input("Informe sua opcao: "))
        except :
            print("\nErro! Informe um número entre 1-5 ou 9 para sair")
            continue
        match opcao :
            case 1 :
                palavra = input("Informe palavra para adicionar: ")
                traducao = input("Informe traducao: ")
                print(incluir_palavra(palavra, traducao))
            case 2 :
                palavra = input("Informe palavra a alterar: ")
                traducao = input("Informe traducao: ")
                print(alterar_traducao(palavra, traducao))
            case 3 :
                palavra = input("Informe palavra a remover: ")
                print(remover_palavra(palavra))
            case 4 :
                palavra = input("Informe palavra a traduzir: ")
                print(traduzir(palavra))
            case 5 :
                print(listar_palavras())
            case 9 :
                print("Finalizando")
                gravar("dicionario.json")
                break
  
# programa principal
main()