#Separar cada palavra que forma a frase "A ligeira raposa marrom ataca o cão preguiçoso". Quantas palavras formam esta frase ?

txt = "A ligeira raposa marrom ataca o cão preguiçoso"
separado = (txt.split(" "))
qtd = len(separado)

print(separado)
print(f"A frase tem {qtd} palavras")