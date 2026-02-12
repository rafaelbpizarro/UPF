txt = str(input("Escreva qualquer texto: "))
car = str(input("O que você quer concatenar ao texto? "))
local = str(input("No início ou no final? "))

if local == "início" or local == "Início" or local == "inicio" or local == "Inicio":
    concatenar = (car, txt)
elif local == "final" or local == "Final":
    concatenar = (txt, car)


print(concatenar)