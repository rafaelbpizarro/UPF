#Leia um valor inteiro e em seguida apresente uma mensagem que diga se o número é PAR ou ÍMPAR
numero = int(input("Digite um número inteiro: "))
if numero == 0:
    print("Seu número é 0")
elif numero % 2 == 0:
    print("Seu número é Par")
else:
    print("Seu número é Ímpar")
    