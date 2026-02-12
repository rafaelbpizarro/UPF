txt = str(input("Escreva qualquer texto: "))

if txt.isalpha():
    print(f'"{txt}"é composto apenas de caracteres alfabéticos')
elif txt.isdigit():
    print(f'"{txt}" é composto apenas de números')
else:
    print(f'"{txt}" é composto de letras e números')