nome = input("Qual seu nome? ")
dia = int(input("Qual o dia do seu aniversário? "))
mes = int(input("Qual o mês do seu aniversário? "))

if dia >= 21 and dia <= 31 and mes == 1 or dia >= 1 and dia <= 18 and mes == 2:
    signo = "Aquário"
elif dia >= 19 and dia <= 29 and mes == 2 or dia >= 1 and dia <= 20 and mes == 3:
    signo = "Peixes"
elif dia >= 21 and dia <= 31 and mes == 3 or dia >= 1 and dia <= 20 and mes == 4:
    signo = "Áries"
elif dia >= 21 and dia <= 30 and mes == 4 or dia >= 1 and dia <= 21 and mes == 5:
    signo = "Touro"
elif dia >= 22 and dia <= 31 and mes == 5 or dia >= 1 and dia <= 21 and mes == 6:
    signo = "Gêmeos"
elif dia >= 22 and dia <= 30 and mes == 6 or dia >= 1 and dia <= 22 and mes == 7:
    signo = "Câncer"
elif dia >= 23 and dia <= 31 and mes == 7 or dia >= 1 and dia <= 23 and mes == 8:
    signo = "Leão"
elif dia >= 24 and dia <= 31 and mes == 8 or dia >= 1 and dia <= 22 and mes == 9:
    signo = "Virgem"
elif dia >= 23 and dia <= 30 and mes == 9 or dia >= 1 and dia <= 23 and mes == 10:
    signo = "Libra"
elif dia >= 24 and dia <= 31 and mes == 10 or dia >= 1 and dia <= 22 and mes == 11:
    signo = "Escorpião"
elif dia >= 23 and dia <= 30 and mes == 11 or dia >= 1 and dia <= 21 and mes == 12:
    signo = "Sagitário"  
elif dia >= 22 and dia <= 31 and mes == 12 or dia >= 1 and dia <= 20 and mes == 1:
    signo = "Capricórnio"
else:
    print("ERRO, DATA INVÁLIDA")
    exit()

print(f"Seu nome é {nome}, seu aniversário é {dia}/{mes} e seu signo é {signo}")