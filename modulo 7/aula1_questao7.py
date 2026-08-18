import random


def encrypt(nomes):
    """Retorna os nomes criptografados e a chave aleatória usada."""
    chave = random.randint(1, 10)
    inicio_visivel = 33
    total_caracteres_visiveis = 94

    nomes_criptografados = []
    for nome in nomes:
        nome_criptografado = ""
        for caractere in nome:
            codigo = ord(caractere)
            if inicio_visivel <= codigo <= 126:
                codigo_criptografado = (
                    inicio_visivel
                    + (codigo - inicio_visivel + chave) % total_caracteres_visiveis
                )
                nome_criptografado += chr(codigo_criptografado)
            else:
                nome_criptografado += caractere
        nomes_criptografados.append(nome_criptografado)

    return nomes_criptografados, chave


if __name__ == "__main__":
    nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
    nomes_cript, chave_aleatoria = encrypt(nomes)

    print(f"Chave de criptografia: {chave_aleatoria}")
    print(f"Nomes criptografados: {nomes_cript}")
