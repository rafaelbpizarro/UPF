entrada1 = input("Escreva uma lista de 10 componentes separados por espaço ou vírgula: ")
entrada1 = entrada1.replace(",", " ")
lista1 = entrada1.split()
if len(lista1) != 10:
    exit("A lista deve ter 10 componentes")
else:
    entrada2 = input("\nEscreva outra lista de 10 componentes separados por espaço ou vírgula: ")
    entrada2 = entrada2.replace(",", " ")
    lista2 = entrada2.split()
    if len(lista2) != 10:
        exit("A lista deve ter 10 componentes")
    else:
        lista3 = []
        for i in range(10):
            lista3.append(lista1[i])
            lista3.append(lista2[i])
            
        print(f"\nLista 3(Elementos Intercalados):\n{lista3}")