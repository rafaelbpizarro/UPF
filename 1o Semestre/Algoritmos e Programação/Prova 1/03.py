'''
Um concurso da loteria irá pagar 2000000,00...
62%      primeira faixa        seis acertos (sena)
22%      segunda faixa         cinco acertos (quina)
16%      terceira faixa        quatro acertos (quadra)
'''

premioTotal = 2000000
sena = premioTotal * 0.62
quina = premioTotal * 0.22
quadra = premioTotal * 0.16

qtdsena = int(input("Quantas pessoas ganharam a sena? "))
qtdquina = int(input("Quantas pessoas ganharam a quina? "))
qtdquadra = int(input("Quantas pessoas ganharam a quadra? "))

premiosena = sena // qtdsena
premioquina = quina // qtdquina
premioquadra = quadra // qtdquadra

print(f"Os ganhadores da sena recebem R${premiosena:.2f}, os ganhadores da quina recebem R${premioquina:.2f} e os ganhadores da quadra recebem R${premioquadra:.2f}.")