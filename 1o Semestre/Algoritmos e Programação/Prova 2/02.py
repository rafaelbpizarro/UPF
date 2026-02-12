#2. Elabore um algoritmo com implementação em Python que recebe
#duas listas e retorna uma nova lista contendo apenas os elementos
#únicos presentes em ambas as listas, sem repetições.
lista1 = set()
lista2 = set()

tamanho = int(input("Quantos números a lista 1 terá? "))
if tamanho < 1:
    print("a lista deve ter pelo menos um número\n")
else:
    for x in range((tamanho)):
        numero1 = float(input(f"Adicione o {x + 1}º número: "))
        lista1.add(numero1)
        print(f'"{numero1}" adicionado a lista 1\n')
        
tamanho = int(input("Quantos números a lista 2 terá? "))
if tamanho < 1:
    print("a lista deve ter pelo menos um número\n")
else:
    for x in range((tamanho)):
        numero2 = float(input(f"Adicione o {x + 1}º número: "))
        lista2.add(numero2)
        print(f'"{numero2}" adicionado a lista 2\n')


intersecao = lista1.intersection(lista2)
print(f"Lista 1: {lista1}\nLista 2: {lista2}") 
print(f"Interseção das listas 1 e 2: {intersecao}\n")
