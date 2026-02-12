meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temp = []

for x in range(12):
    temp.insert(x, float(input(f"\nInforme a temperatura média (ºC) no mês de {meses[x]}: ")))

media = 0
for x in range(12):
    media += temp[x]
media = media / 12

print("\n\nTemperaturas acima da média anual e seus respectivos meses:")

for x in range(12):
    if temp[x] >= media:
        print(f"{temp[x]}ºC - {meses[x]}")