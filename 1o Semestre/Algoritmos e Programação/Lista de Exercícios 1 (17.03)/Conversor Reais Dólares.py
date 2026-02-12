print("Conversão Reais para Dólar")
valor = float(input("Qual o valor (em reais) a ser convertido ? "))
dolar = float(input("Qual a cotação do dia? "))
Resultado = float((valor / dolar))
txt = f"Valor em dolares: USD {Resultado:.2f}"
print(txt)
