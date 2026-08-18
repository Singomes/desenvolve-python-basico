frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"

frase_modificada = ""
for caractere in frase:
    if caractere in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += caractere

print(f"Frase modificada: {frase_modificada}")