frase = input("Digite uma frase: ")

vogais = sorted ([char.lower() for char in frase if char.lower() in 'aeiouáéíóúâêîôûãõ'])

consoantes = [char for char in frase if char.isalpha() and char.lower() not in 'aeiouáéíóúâêîôûãõ']

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
