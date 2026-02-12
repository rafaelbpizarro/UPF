nome1 = input("Qual o primeiro nome? ")
idade1 = int(input(f"Qual a idade de {nome1}? "))
nome2 = input("Qual o segundo nome? ")
idade2 = int(input(f"Qual a idade de {nome2}? "))
nome3 = input("Qual o terceiro nome? ")
idade3 = int(input(f"Qual a idade de {nome3}? "))


if idade1 > idade2 and idade1 > idade3:
    maior = idade1
elif idade2 > idade1 and idade2 > idade3:
    maior = idade2
elif idade3 > idade1 and idade3 > idade2:
    maior = idade3
    
if idade1 < idade2 and idade1 < idade3:
    menor = idade1
elif idade2 < idade1 and idade2 < idade3:
    menor = idade2
elif idade3 < idade1 and idade3 < idade2:
    menor = idade3
    
if maior == idade1:
        print(f"O mais velho é {nome1}, com {idade1} ano(s) e")
elif maior == idade2:
        print(f"O mais velho é {nome2}, com {idade2} ano(s) e")
elif maior == idade3:
        print(f"O mais velho é {nome3}, com {idade3} ano(s) e")
    
if menor == idade1:
        print(f"o mais novo é {nome1}, com {idade1} ano(s)")
elif menor == idade2:
        print(f"o mais novo é {nome2}, com {idade2} ano(s)")
elif menor == idade3:
        print(f"o mais novo é {nome3}, com {idade3} ano(s)")