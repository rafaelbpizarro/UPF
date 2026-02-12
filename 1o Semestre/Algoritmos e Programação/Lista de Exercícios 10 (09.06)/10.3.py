# declaracao de variaveis globais
velha = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

jogador = 'O'
contaJogadas = 1

# exemplo de laco para percorrer matriz e
def mostraTabuleiro() :
    print()
    for i in range (3) :
        for j in range (3) :
            print(velha[i][j], end="") # imprime caractere sem avancar a linha
            print(" | ", end="")
        if (i < 2 ) :
            print("\n--|---|---")
    print()
                        
def validaJogada(pos) :
    match pos :
        case 1 : linha = 0; coluna = 0
        case 2 : linha = 0; coluna = 1
        case 3 : linha = 0; coluna = 2
        case 4 : linha = 1; coluna = 0
        case 5 : linha = 1; coluna = 1
        case 6 : linha = 1; coluna = 2
        case 7 : linha = 2; coluna = 0
        case 8 : linha = 2; coluna = 1
        case 9 : linha = 2; coluna = 2
    
    if velha[linha][coluna] in ['O','X'] :
        return False
    else :
        velha[linha][coluna] = jogador
        return True

def temVencedor() :
    # verifica linhas
    if ((velha[0][0] == velha[0][1] and velha[0][1] == velha[0][2]) or
        (velha[1][0] == velha[1][1] and velha[1][1] == velha[1][2]) or
        (velha[2][0] == velha[2][1] and velha[2][1] == velha[2][2]) or
    # verifica colunas
        (velha[0][0] == velha[1][0] and velha[1][0] == velha[2][0]) or
        (velha[0][1] == velha[1][1] and velha[1][1] == velha[2][1]) or
        (velha[0][2] == velha[1][2] and velha[1][2] == velha[2][2]) or
    # verifica transversais
        (velha[0][0] == velha[1][1] and velha[1][1] == velha[2][2]) or
        (velha[0][2] == velha[1][1] and velha[1][1] == velha[2][0])) :
            mostraTabuleiro()
            return True
    else :
        return False
        
    
# programa principal
while True :
    mostraTabuleiro()
    try :
        pos = int(input(f"Jogador {jogador}, escolha a posição da jogada: "))
    except :
        print("\n\nPosicao informada inválida!\n")
        continue

    # chamada da funcao que valida a jogada
    if not validaJogada(pos) :
        print("\nPosicao ja está ocupada, jogue novamente! \n")
        continue

    if temVencedor() :
        print(f"\n\nParabens Jogador {jogador} Venceu !!! \n")
        break

    # troca jogador
    if jogador == 'O' :
        jogador = 'X'
    else :
        jogador = 'O'

    # incrementa numero de jogadas
    contaJogadas += 1
    
    # verifica situacao de empate
    if contaJogadas > 9 :
        print("\n\nEmpate !\n")
        break
