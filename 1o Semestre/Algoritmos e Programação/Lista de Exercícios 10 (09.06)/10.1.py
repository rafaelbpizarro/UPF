import random
numero = random.randint(0, 101)
chances = 5
print ("Adivinhe o numero!")
while True :
    print(f"Voce tem {chances} chances")
    palpite = int(input("Qual seu palpite ? "))
    if (palpite == numero) :
        print("Parabéns! Voce acertou! ")
        break
    elif (palpite < numero) :
        print("É um número maior")
    else :
        print("É um número menor")
    # decrementa o numero de chances
    chances -= 1
    if (chances == 0) :
        print(f"Voce perdeu! O numero era {numero}")
        break
