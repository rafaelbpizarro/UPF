txt = str(input("Escreva qualquer texto: "))
car1 = str(input("Escolha o caracter a ser substituido: "))
car2 = str(input(f'Escolha o caracter que substituirá "{car1}": '))

print(txt.replace(f"{car1}", f"{car2}"))