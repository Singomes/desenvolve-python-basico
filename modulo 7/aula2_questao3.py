while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')

    if frase.strip().lower() == "fim":
        break

    frase_normalizada = "".join(
        caractere.lower() for caractere in frase if caractere.isalnum()
    )

    if frase_normalizada == frase_normalizada[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')