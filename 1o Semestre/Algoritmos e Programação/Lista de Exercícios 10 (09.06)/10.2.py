import random
palavras = ["ovo", "banana", "maçã", "cenoura", "tomate"]

def escolher_palavra():
    # palavra_aleatoria = random.choice(palavras)
    return random.choice(palavras)
    
def mostrar_palavra_oculta(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

palavra = escolher_palavra()
letras_corretas = []
tentativas_maximas = 6
tentativas = 0

print(mostrar_palavra_oculta(palavra, letras_corretas))

while tentativas < tentativas_maximas:
    palpite = input("Digite uma letra: ").lower()

    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, digite apenas uma letra válida.")
        continue

    if palpite in letras_corretas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    if palpite in palavra:
        letras_corretas.append(palpite)
        print("Letra correta!")
        print(mostrar_palavra_oculta(palavra, letras_corretas))
    else:
        tentativas += 1
        print("Letra incorreta. Tentativas restantes: {}".format(tentativas_maximas - tentativas))

        print(mostrar_palavra_oculta(palavra, letras_corretas))

    if set(letras_corretas) == set(palavra):
        print("Parabéns! Você acertou a palavra: '{}'".format(palavra))
        break

    if tentativas == tentativas_maximas:
        print("Você perdeu! A palavra correta era '{}'.".format(palavra))
        
        
        