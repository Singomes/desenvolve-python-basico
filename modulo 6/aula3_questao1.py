numeros = []

print("Digite os números inteiros (digite 'sair' para encerrar):")

while True:
    entrada = input(">")
    if entrada.lower() == 'sair':
        if len(numeros) < 4:
            print("Por favor, insira pelo menos 4 números.")
            continue
        break
    try:
        numeros.append(int(entrada))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro ou 'sair'.")

        print(f"\nA lista original: {numeros}")
        print(f"Os tres primeiros elementos: {numeros[:3]}")
        print(f"Os dois ultimos elementos: {numeros[-2:]}")
        print(f"A lista invertida: {numeros[::-1]}")
        print(f"Os elementos de índice par (0, 2, 4...): {numeros[::2]}")
        print(f"Os elementos índice impar(1 ,3 ,5...): {numeros[1::2]}")
        
          