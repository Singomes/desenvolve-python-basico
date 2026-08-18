frase = input("Digite uma frase: ")
indices = []

for indice, letra in enumerate(frase):
    if letra.lower() in "aeiou":
        indices.append(indice)

print(f"{len(indices)} vogais")
print(f"Índices {indices}")