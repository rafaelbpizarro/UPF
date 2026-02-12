a = float(input("Escolha o primeiro valor: "))
b = float(input("Escolha o segundo valor: "))
c = float(input("Escolha o terceiro valor: "))

if (a + b) < c or (b + c) < a or (a + c) < b:
    print("Não forma triângulo")
    exit()
elif a == 0 or b == 0 or c == 0:
    print("ERRO")
    exit()
elif a == b == c:
    print("O Triângulo é Equilátero")
elif a == b or a == c or b == c:
    print("O Triângulo é Isósceles")
elif a != b != c != a:
    print("O Triângulo é Escaleno")
else:
    print("ERRO")
    exit()