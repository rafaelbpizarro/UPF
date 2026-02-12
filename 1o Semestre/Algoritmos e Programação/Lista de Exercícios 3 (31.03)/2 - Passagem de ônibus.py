normal = float(input("Insira o valor da passagem de ônibus (sem descontos): R$"))
qtd = int(input("Quantas passagens você quer comprar? "))
estudante = (normal * 0.6)

if qtd == 0 or normal == 0:
    print("Valor Inválido")
    exit()
elif qtd <= 50:
    total = qtd * estudante
    print(f"{qtd} passagens pelo valor de estudante({estudante})")
    print(f"Total = {total} ")
elif qtd > 50:
    resto = (qtd - 50)
    total = (50) * (estudante) + resto * normal
    print(f"50 passagens pelo valor de estudante (R${estudante:.2f}) e {resto} pelo valor normal (R${normal:.2f})")
    print(f"Total = R${total:.2f} ")