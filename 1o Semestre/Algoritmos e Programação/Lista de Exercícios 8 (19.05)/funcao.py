def dataPorExtenso (ddmmyyyy):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",\
             "agosto", "setembro", "outubro", "novembro", "dezembro"]
    dd= ddmmyyyy[:2]
    mm = int(ddmmyyyy[3:5])
    yyyy = ddmmyyyy[6:10]
    
    return dd + " de " + meses[mm-1] + " de " + yyyy

def converter12h(hora, minuto):
    if not (0 <= hora <= 23 and 0 <= minuto <= 59):
        return exit("Horário incorreto, por favor insira um horário entre 00:00 e 23:59")
    sufixo = "A.M." if hora < 12 else "P.M."
    hora_12 = hora % 12
    if hora_12 == 0:
        hora_12 = 12
    return f"{hora_12}:{minuto:02d} {sufixo}"


def TipoDeTriangulo(a, b, c):
    lados = sorted([a, b, c])
    if lados[0] + lados[1] <= lados[2]:
        return "Não é um triângulo"
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

def NomeEstado(sigla):
    estados = {
        "AC": "Acre",
        "AL": "Alagoas",
        "AP": "Amapá",
        "AM": "Amazonas",
        "BA": "Bahia",
        "CE": "Ceará",
        "DF": "Distrito Federal",
        "ES": "Espírito Santo",
        "GO": "Goiás",
        "MA": "Maranhão",
        "MT": "Mato Grosso",
        "MS": "Mato Grosso do Sul",
        "MG": "Minas Gerais",
        "PA": "Pará",
        "PB": "Paraíba",
        "PR": "Paraná",
        "PE": "Pernambuco",
        "PI": "Piauí",
        "RJ": "Rio de Janeiro",
        "RN": "Rio Grande do Norte",
        "RS": "Rio Grande do Sul",
        "RO": "Rondônia",
        "RR": "Roraima",
        "SC": "Santa Catarina",
        "SP": "São Paulo",
        "SE": "Sergipe",
        "TO": "Tocantins"
    }
    return estados.get(sigla.upper(), "UF inválido")

def EstaOrdenada(lista):
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))

def Primo(n):
    if n <= 1:
        return "Não é primo"
    if n == 2:
        return "É primo"
    if n % 2 == 0:
        return "Não é primo"
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return "Não é primo"
    return "É primo"