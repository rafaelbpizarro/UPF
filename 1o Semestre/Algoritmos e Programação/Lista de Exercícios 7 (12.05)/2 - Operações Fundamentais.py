conjunto1 = set()
conjunto2 = set()

while True:
    print("Opções:\na. alterar conjunto 1\nb. alterar conjunto 2\nc. união entre conjuntos\nd. interseção entre conjuntos\ne. diferença entre conjuntos\nf. obter o tamanho do conjunto\ng. obter o valor máximo e mínimo do conjunto\nh. encerrar programa\n")
    opcao = input("Informe sua opção: ")
    minusculo = opcao.lower()
    if minusculo != 'a' and minusculo != 'b' and minusculo != 'c' and minusculo != 'd' and minusculo != 'e' and minusculo != 'f' and minusculo != 'g' and minusculo != 'h':
        print(f'\n"{opcao}" não é uma opção válida\n')
    else:
#a. ALTERAR CONJUNTO 1
        if minusculo == 'a':
            conjunto1.clear()
            tamanho = int(input("Quantos números o conjunto 1 terá? "))
            if tamanho < 1:
                print("o conjunto deve ter pelo menos um número\n")
            else:
                for x in range((tamanho)):
                    numero = float(input(f"Adicione o {x + 1}º número: "))
                    conjunto1.add(numero)
                    print(f'"{numero}" adicionado ao conjunto 1\n')
#b. ALTERAR CONJUNTO 2
        if minusculo == 'b':
            conjunto2.clear()
            tamanho = int(input("Quantos números o conjunto 2 terá? "))
            if tamanho < 1:
                print("o conjunto deve ter pelo menos um número\n")
            else:
                for x in range((tamanho)):
                    numero = float(input(f"Adicione o {x + 1}º número: "))
                    conjunto2.add(numero)
                    print(f"{numero} adicionado ao conjunto 2\n")
#c. UNIÃO ENTRE CONJUNTOS
        if minusculo == 'c':
            if len(conjunto1) < 1 and len(conjunto2) < 1:
                print('\nAmbos os conjuntos estão vazios, altere-os nas opções "a." e "b."\n')
            else:
                conjunto3 = conjunto1.union(conjunto2)
                print(f"União dos conjuntos 1 e 2: {conjunto3}\n")
#d. INTERSEÇÃO ENTRE CONJUNTOS
        if minusculo == 'd':
            if len(conjunto1) < 1 or len(conjunto2) < 1:
                print("Os dois conjuntos devem possuir algum elemento para fazer a interseção")
            else:
                conjunto3 = conjunto1.intersection(conjunto2)
                if len(conjunto3) < 1:
                    print("Não existem números iguais nos dois conjuntos\n")
                else:
                    print(f"Interseção dos conjuntos 1 e 2: {conjunto3}\n")
#e. DIFERENÇA ENTRE CONJUNTOS
        if minusculo == 'e':
            if len(conjunto1) < 1 or len(conjunto2) < 1:
                print("Os dois conjuntos devem possuir algum elemento para fazer a diferença")
            else:
                conjunto3 = conjunto1.difference(conjunto2)
                print(f"Diferença dos conjuntos 1 e 2: {conjunto3}\n")
#f. OBTER O TAMANHO DO CONJUNTO
        if minusculo == 'f':
            qual = int(input("Qual conjunto você quer saber o tamanho (1, 2 ou 3(última operação realizada))? "))
            if qual != 1 and qual != 2 and qual != 3:
                print("Selecione um conjunto existente!")
            elif qual == 1:
                print(f"O conjunto 1 possui {len(conjunto1)} elementos\n")
            elif qual == 2:
                print(f"O conjunto 2 possui {len(conjunto2)} elementos\n")
            elif qual == 3:
                print(f"A última operação realizada possui {len(conjunto3)} elementos\n")
#g. OBTER O VALOR MÁXIMO E MÍNIMO DO CONJUNTO
        if minusculo == 'g':
            qual = int(input("Qual conjunto você quer obter os valores máximo e mínimo (1, 2 ou 3(última operação realizada))? "))
            if qual != 1 and qual != 2 and qual != 3:
                print("Selecione um conjunto existente!")
            elif qual == 1:
                if len(conjunto1) < 1:
                    print("O conjunto está vazio")
                else:
                    print(f"Valor máximo: {max(conjunto1)}\nValor mínimo: {min(conjunto1)}\n")
            elif qual == 2:
                if len(conjunto2) < 1:
                    print("O conjunto está vazio")
                else:
                    print(f"Valor máximo: {max(conjunto2)}\nValor mínimo: {min(conjunto2)}\n")
            elif qual == 3:
                if len(conjunto3) < 1:
                    print("Nenhuma operação foi realizada")
                else:
                    print(f"Valor máximo: {max(conjunto3)}\nValor mínimo: {min(conjunto3)}\n")
#h. ENCERRAR PROGRAMA
        if minusculo == 'h':
            encerrar = (input("Tem certeza que quer encerrar o programa? (Sim ou Não)"))
            minusculo2 = encerrar.casefold()
            if minusculo2 != "não" and minusculo2 != "nao" and minusculo2 != "sim":
                print('\nDigite apenas "Sim" ou "Não"\n')
            elif minusculo2 == "não" or minusculo2 == "nao":
                print("\nO programa permanece ativo.\n")
            elif minusculo2 == "sim":
                break
exit("Programa encerrado")