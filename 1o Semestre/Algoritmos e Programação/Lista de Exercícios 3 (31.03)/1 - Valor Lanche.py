print("Cod	Descrição	Preço em R$")
print("10	Cachorro-quente	1.10")
print("11	Bauru simples	1.30")
print("12	Bauru com ovo	1.50")
print("13	Hamburguer	1.10")
print("14	Cheeseburger	1.30")
print("15	Refrigerante	1.50")

opcao = int(input("Informe sua opção: "))
match opcao:
    case 10 | 13:
        preco = 1.1
    case 11 | 14:
        preco = 1.3
    case 12 | 15:
        preco = 1.5
    case other:
        print("Opção Inválida")
        exit()
        
qtd = int(input("Informe a quantidade: "))
total = preco * qtd
print(f"O Total será R${total:.2f}")