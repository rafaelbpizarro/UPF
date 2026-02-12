correta = "2023"
tentativas = 0

while True:
    senha = input("Digite a senha: ")
    tentativas += 1
    
    if  senha == correta:
        print("\nACESSO PERMITIDO\n")
        break
    else:
        print("\nSENHA INVÁLIDA\n")


print(f"Tentativas: {tentativas}")
