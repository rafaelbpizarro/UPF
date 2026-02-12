valor = int(input("Valor em reais: "))

n100 = int(valor / 100)
resto = valor - (n100 * 100)

n50 = int(resto / 50)
resto = resto - (n50 * 50)

n20 = int(resto / 20)
resto = resto - (n20 * 20)

n10 = int(resto / 10)
resto = resto - (n10 * 10)

if valor % 2 != 0:
    n5 = resto // 5
    resto = resto - (n5 * 5)
else:
    n5 = 0

n2 = resto // 2
resto = resto - (n2 * 2)

print(valor, "pode ser decomposto em: ")
print(n100, "nota(s) de 100 reais;")
print(n50, "nota(s) de 50 reais;")
print(n20, "nota(s) de 20 reais;")
print(n10, "nota(s) de 10 reais;")
print(n5, "nota(s) de 5 reais e")
print(n2, "nota(s) de 2 reais;")