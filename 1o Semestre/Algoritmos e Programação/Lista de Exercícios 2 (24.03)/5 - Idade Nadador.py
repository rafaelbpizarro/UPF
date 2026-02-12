idade = int(input("Qual a sua idade? "))
if 4 < idade < 8:
    print("Você se encaixa na categoria Infantil A")
elif 7 < idade < 11:
    print("Você se encaixa na categoria Infantil B")
elif 10 < idade < 14:
    print("Você se encaixa na categoria Juvenil A")
elif 13 < idade < 18:
    print("Você se encaixa na categoria Juvenil B")
elif idade > 18:
    print("Você se encaixa na categoria Adulto")