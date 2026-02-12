dia = int(input("Informe um dia: "))
mes = int(input("Informe um mês (1 a 12): "))
ano = int(input("Informe um ano (0 a 3000): "))

if ano >= 0 and ano <= 3000:
    vddano = True
elif ano < 0 or ano > 3000:
    vddano = False

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    bissexto = True
else:
    bissexto = False



if 1 <= mes <= 12:
    vddmes = True
else:
    vddmes = False
    
if mes == 2:
    if bissexto == True:
        fev29 = True
    else:
        fev29 = False
else:
    fev29 = False
    
if fev29 == True and 1 <= dia <= 29:
    vdddia = True
elif fev29 == False and dia < 1 or fev29 == False and dia > 28:
    vdddia = False
elif fev29 == False and 1 <= dia <= 28:
    vdddia = True
elif fev29 == True and dia < 1 or fev29 == False and dia > 29:
    vdddia = False


if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dia30 = True
elif mes == 1 or mes == 2 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dia30 = False

if dia30 == True and mes != 2 and dia >= 1 and dia <= 30:
    vdddia = True
elif dia30 == False and mes != 2 and dia >= 1 and dia <= 31:
    vdddia = True
    
if vddano == True and vddmes == True and vdddia == True:
    print(f"A Data {dia}/{mes}/{ano} é Válida.")
elif vddano == 0 or vddmes == 0 or vdddia == 0:
    print(f"A Data Informada é Inválida.")