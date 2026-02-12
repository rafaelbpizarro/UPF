#Professor, utilizei == ao invés do in para aceitar apenas respostas de Sim ou Não ao invés de qualquer texto que contiver as palavras "Sim" e "Não"
classificacao = 0


print("Por favor responda a todas as perguntas da investigação apenas com Sim ou Não.")



pergunta1 = str(input("\nTelefonou para a vítima? "))

if "Sim" == pergunta1 or "sim" == pergunta1: #<---- in
    classificacao += 1
    print("")
elif "Não" == pergunta1 or "não" == pergunta1 or "Nao" == pergunta1 or "nao" == pergunta1:
    print("")
else:
    exit("RESPONDA APENAS COM SIM OU NÃO")



pergunta2 = str(input("Esteve no local do crime? "))

if "Sim" == pergunta2 or "sim" == pergunta2:
    classificacao += 1
    print("")
elif "Não" == pergunta2 or "não" == pergunta2 or "Nao" == pergunta2 or "nao" == pergunta2:
    print("")
else:
    exit("RESPONDA APENAS COM SIM OU NÃO")



pergunta3 = str(input("Mora perto da vítima? "))

if "Sim" == pergunta3 or "sim" == pergunta3:
    classificacao += 1
    print("")
elif "Não" == pergunta3 or "não" == pergunta3 or "Nao" == pergunta3 or "nao" == pergunta3:
    print("")
else:
    exit("RESPONDA APENAS COM SIM OU NÃO")



pergunta4 = str(input("Devia para a vítima? "))

if "Sim" == pergunta4 or "sim" == pergunta4:
    classificacao += 1
    print("")
elif "Não" == pergunta4 or "não" == pergunta4 or "Nao" == pergunta4 or "nao" == pergunta4:
    print("")
else:
    exit("RESPONDA APENAS COM SIM OU NÃO")



pergunta5 = str(input("Já trabalhou com a vítima? "))

if "Sim" == pergunta5 or "sim" == pergunta5:
    classificacao += 1
    print("")
elif "Não" == pergunta5 or "não" == pergunta5 or "Nao" == pergunta5 or "nao" == pergunta5:
    print("")
else:
    exit("RESPONDA APENAS COM SIM OU NÃO")


if classificacao == 5:
    resultado = "Assassino"
elif 3 <= classificacao <= 4:
    resultado = "Cúmplice"
elif classificacao >= 2:
    resultado = "Suspeita"
else:
    resultado = "Inocente"

print(f"Resultado final: {resultado}")