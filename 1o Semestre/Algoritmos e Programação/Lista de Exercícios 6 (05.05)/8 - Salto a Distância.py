saltos = []
numero = "Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"

print('Para encerrar o programa deixe o campo "nome do atleta" em branco e envie')

while True:
    saltos.clear()
    atleta = str(input("Atleta: "))
    if atleta == "":
        break
    else:
        for x in range(5):
            saltos.insert(x, float(input(f"{numero[x]} salto: ")))
    
        media = sum(saltos) / len(saltos)

    print(f"\nResultado final: \nAtleta: {atleta} \nSaltos: {saltos[0]}m - {saltos[1]}m - {saltos[2]}m - {saltos[3]}m - {saltos[4]}m \nMédia dos saltos: {media}m\n")

print("\nNome não informado, encerrando programa...")
exit()