import json

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

letras_objetivo = sorted(palavra_objetivo.lower())
anagramas = []

for palavra in frase.split():
    palavra_limpa = palavra.strip(".,;:!?()[]{}\"'")
    if sorted(palavra_limpa.lower()) == letras_objetivo:
        anagramas.append(palavra_limpa)

anagramas.sort(key=str.lower)
print(f"Anagramas: {json.dumps(anagramas, ensure_ascii=False)}")