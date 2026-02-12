a = int(input("Escolha um valor: "))
b = int(input("Escolha um segundo valor: "))
c = int(input("Escolha um terceiro valor: "))

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
    
if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
    
intermediario = a + b + c - menor - maior

print(f"O maior valor é {maior}, o menor é {menor} e o intermediário é {intermediario}.")