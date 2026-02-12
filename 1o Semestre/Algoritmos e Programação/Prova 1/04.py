'''
Uma empresa avalia o desempenho...

Pontualidade     Produtividade     Desempenho
>= 90                 >= 8         Excelente
>= 90                 < 8             Bom
70 a 89               >= 6          Regular
70 a 89               < 6             Ruim
<70                 Qualquer     Insatisfatório
'''

pontualidade = str(input("Qual a pontualidade do funcionário? (de 0% a 100%)"))
produtividade = float(input("Qual a produtividade do funcionário? (de 0 a 10)"))

if "%" not in pontualidade:
    desempenho = 'ERRO: Porcentagem inválida (utilize o símbolo "%")'
    print(desempenho)
    exit()
else:
    pontualidade = int((pontualidade.replace("%", "")))

if pontualidade < 0 or pontualidade > 100 or produtividade > 10 or produtividade < 0:
    desempenho = "ERRO: Valor Inválido"
    print(desempenho)
    exit()
elif pontualidade >= 90 and produtividade >= 8:
    desempenho = "Excelente"
elif pontualidade >= 90 and produtividade < 8:
    desempenho = "Bom"
elif 70 <= pontualidade <= 89 and produtividade >= 6:
    desempenho = "Regular"
elif 70 <= pontualidade <= 89 and produtividade < 6:
    desempenho = "Ruim"
elif pontualidade < 70:
    desempenho = "Insatisfatório"
else:
    desempenho = "ERRO"
    print(desempenho)
    exit()

print(f"Pontualidade: {pontualidade}%")
print(f"Produtividade: {produtividade}")
print(f"Desempenho: {desempenho}")