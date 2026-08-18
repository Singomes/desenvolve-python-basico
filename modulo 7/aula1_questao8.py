import re


def calcula_digito(numeros, multiplicadores):
    soma = sum(numero * multiplicador for numero, multiplicador in zip(numeros, multiplicadores))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def cpf_valido(cpf):
    if not re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
        return False

    digitos = [int(digito) for digito in re.sub(r"\D", "", cpf)]
    if len(set(digitos)) == 1:
        return False

    primeiro_digito = calcula_digito(digitos[:9], range(10, 1, -1))
    segundo_digito = calcula_digito(
        digitos[:9] + [primeiro_digito], range(11, 1, -1)
    )

    return digitos[9:] == [primeiro_digito, segundo_digito]


if __name__ == "__main__":
    cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
    print("Válido" if cpf_valido(cpf) else "Inválido")
