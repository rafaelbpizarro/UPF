compras = set()
ordem_alfabetica = []

while True:
    print("Opções:\na. adicionar item\nb. remover item\nc. exibir todos os itens\nd. ordernar o conjunto alfabeticamente\ne. verificar se um item está contido em um conjunto\nf. gravar a lista de compras em um arquivo\ng. ler a lista de compras de um arquivo e traze-lo para a run atual\nh. encerrar programa (lembre-se de salvar o arquivo antes de encerrar).\n")
    opcao = input("Informe sua opção: ")
    minusculo = opcao.lower()
    if minusculo != 'a' and minusculo != 'b' and minusculo != 'c' and minusculo != 'd' and minusculo != 'e' and minusculo != 'f' and minusculo != 'g' and minusculo != 'h':
        print(f'"{opcao}" não é uma opção válida')
    else:
#OPCAO A
        if minusculo == 'a':
            item = input("Informe item a adicionar: ")
            if item in compras:
                print(f'\n"{item}" já está no conjunto!\n')
            else:
                compras.add(item)
                print(f'\n"{item}" foi adicionado a lista com sucesso!\n')
#OPCAO B
        if minusculo == 'b':
            if len(compras) == 0:
                print("\nA Lista está vazia\n")
            else:
                item = input("Informe item a remover: ")
                if item not in compras:
                    print(f'\n"{item}" não está na lista!\n')
                else:
                    compras.remove(item)
                    print(f'\n"{item}" foi removido da lista.\n')
#OPCAO C
        if minusculo == 'c':
            if len(compras) == 0:
                print("\nA Lista está vazia\n")
            else:
                print(f"\nLista de Compras:\n{compras}\n")
#OPCAO D
        if minusculo == 'd':
            if len(compras) == 0:
                print("\nA Lista está vazia\n")
            else:
                ordem_alfabetica = sorted(compras)
                print(f"\nLista em ordem alfabética:\n{ordem_alfabetica}\n")
#OPCAO E
        if minusculo == 'e':
            if len(compras) == 0:
                print("\nA Lista está vazia\n")
            else:
                item = input("Informe item para verificar: ")
                if item not in compras:
                    print(f'\n"{item}" não está na lista!\n')
                else:
                    print(f'\n"{item}" está na lista\n')
#OPCAO F
        if minusculo == 'f':
            if len(compras) == 0:
                print("\nA Lista está vazia\n")
            else:
                 with open("padrao lista.txt", "w") as f:
                     f.write("LISTA DE COMPRAS:\n")
                     for item in compras:
                         f.write(f"{item}\n")
                     print("\nLista salva com sucesso.\n")
#OPCAO G
        if minusculo == 'g':
            with open("padrao lista.txt", "r") as g:
                conteudo = g.readlines()
                print("\n" + "".join(conteudo))
                compras = set(item.strip() for item in conteudo if item.strip())
                compras.remove("LISTA DE COMPRAS:")
#OPCAO H
        if minusculo == 'h':
            encerrar = (input("Tem certeza que quer encerrar o programa? (Sim ou Não)"))
            minusculo2 = encerrar.casefold()
            if minusculo2 != "não" and minusculo2 == "nao" and minusculo2 != "sim":
                print('Digite apenas "Sim" ou "Não"')
            elif minusculo2 == "não" or minusculo2 == "nao":
                print("\nO programa permanece ativo.\n")
            elif minusculo2 == "sim":
                break
exit("Programa encerrado")