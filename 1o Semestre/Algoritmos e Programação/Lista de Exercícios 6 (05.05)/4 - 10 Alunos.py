mediasAlunos = []

for i in range(10):
    print(f"\nAluno {i + 1}:")
    nota1 = float(input("Informe a 1ª nota: "))
    nota2 = float(input("Informe a 2ª nota: "))
    nota3 = float(input("Informe a 3ª nota: "))
    nota4 = float(input("Informe a 4ª nota: "))
    if nota1 < 10.1 and nota2 < 10.1 and nota3 < 10.1 and nota4 < 10.1:
        media = (nota1 + nota2 + nota3 + nota4) / 4
        mediasAlunos.append(media)
    else:
        exit("\nNOTAS INVÁLIDAS (Só podem estar entre 0 e 10)")

aprovados = sum(1 for m in mediasAlunos if m >= 7)

print(f"\n{aprovados} alunos foram aprovados")