salario = float(input("Qual seu sálario atual?"))
cargo = str(input("Qual seu cargo?"))
if cargo == "Gerente":
    print("Salário Antigo:", salario)
    print("Novo salário:", salario + (0.1 * salario))
    print("Diferença:", (salario + 0.1 * salario) - salario)
elif cargo == "Engenheiro":
    print("Salário Antigo:", salario)
    print("Novo salário:", salario + (0.2 * salario))
    print("Diferença:", (salario + 0.2 * salario) - salario)
elif cargo == "Técnico":
    print("Salário Antigo:", salario)
    print("Novo salário:", salario + (0.3 * salario))
    print("Diferença:", (salario + 0.3 * salario) - salario)
else:
    print("Salário Antigo:", salario)
    print("Novo salário:", salario + (0.4 * salario))
    print("Diferença:", (salario + 0.4 * salario) - salario)