import random
import re


def embaralhar_palavras(frase):
    def embaralhar(palavra):
        if len(palavra) <= 3:
            return palavra

        letras_internas = list(palavra[1:-1])
        random.shuffle(letras_internas)
        return palavra[0] + "".join(letras_internas) + palavra[-1]

    return re.sub(r"\S+", lambda resultado: embaralhar(resultado.group()), frase)


# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)