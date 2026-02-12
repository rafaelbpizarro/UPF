palavras = {
    'banana': 'Uma fruta amarela e deliciosa.',
    'python': 'Uma linguagem de programação poderosa.',
    'praia': 'Um lugar com areia e água salgada.',
    # Adicione mais palavras e suas dicas conforme necessário
}

import random

def jogo_adivinhacao():
    palavra_secreta = random.choice(list(palavras.keys()))
    dica = palavras[palavra_secreta]
    tentativas = 3
    while tentativas > 0:
        print("Dica:", dica)
        palpite = input("Adivinhe a palavra: ").lower()
        if palpite == palavra_secreta:
            print("Parabéns, você acertou!")
            return
        else:
            tentativas -= 1
            print(f"Incorreto! Você tem {tentativas} tentativas restantes.")
    print("Suas tentativas acabaram. A palavra era:", palavra_secreta)

jogo_adivinhacao()
