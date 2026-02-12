salario = float(input("Qual seu salário anual? "))
aliquota1 = salario * 0.075
aliquota2 = salario * 0.15
aliquota3 = salario * 0.225
aliquota4 = salario * 0.275

if salario <= 17989.80:
    print ("Você não precisa pagar imposto de renda")
elif salario >= 17989.81 and salario <= 26961.00:
    print (f"Você deve pagar R${aliquota1:.2f}")
elif salario >= 26961.01 and salario <= 35948.40:
    print (f"Você deve pagar R${aliquota2:.2f} ")
elif salario >= 35948.41 and salario <= 44918.28:
    print (f"Você deve pagar R${aliquota3:.2f} ")
elif salario > 44918.28:
    print (f"Você deve pagar R${aliquota4:.2f} ")