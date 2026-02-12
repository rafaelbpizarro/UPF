EAD = 0
Semi = 0
Presencial = 0
print("O que você prefere: Aula EAD, Semipresencial ou Presencial?")
while True:
    opcao = str(input("a. para EAD\nb. para Semipresencial\nc. para Presencial\nDigite 0 para mostrar os votos.\n"))
    if opcao == "0":
        break
    elif opcao == "a":
        EAD += 1
        print('Voto contabilizado para "EAD"\n')
    elif opcao == "b":
        Semi += 1
        print('Voto contabilizado para "Semi"\n')
    elif opcao == "c":
        Presencial += 1
        print('Voto contabilizado para "Presencial"\n')
    else:
        print("Escolha uma opção válida\n")
total = EAD + Semi + Presencial
porcentoEAD = EAD*100 / total
porcentoSemi = Semi*100 / total
porcentoPresencial = Presencial*100 / total
print(f"\nQuantidade de participantes: {total}")
print(f"Porcentagem de votos para EAD: {porcentoEAD:.2f}%\nPorcentagem de votos para Semipresencial: {porcentoSemi:.2f}%\nPorcentagem de votos para Presencial: {porcentoPresencial:.2f}%")
