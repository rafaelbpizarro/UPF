#2. Elabore um algoritmo com implementação em Python que leia os
#dados de um arquivo de entrada e escreva os resultados em um
#arquivo de saída, com a seguinte estrutura:

def processar_notas(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
        for linha in entrada:
            dados = linha.strip().split(',')
            nome = dados[0]
            notas = list(map(float, dados[1:4]))
            media = sum(notas) / 3
            if media >= 6:
                situacao = "Aprovado"
            else:
                situacao = "Reprovado"
            
            saida.write(f"Aluno: {nome}, Nota1: {notas[0]}, Nota2: {notas[1]}, Nota3: {notas[2]}, Média: {media:.1f}, Situação: {situacao}\n")

print("Certifique-se de que os arquivos estejam na mesma pasta que o programa")
arquivoleitura = str(input("Digite o nome do arquivo (exemplo.txt) com os nomes e notas dos alunos: "))
arquivosaida = str(input("Digite o nome do arquivo (exemplo.txt) que você deseja inserir a saída (caso ele não exista o mesmo será criado): "))
processar_notas(arquivoleitura, arquivosaida)