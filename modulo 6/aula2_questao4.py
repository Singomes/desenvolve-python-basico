def criar_lista():
    n = int(input(f"Digite a quantidade de elementos: "))
    lista = []
    for i in range(n):
        elemento = int(input(f"Digite o elemento {i+1}: "))
        lista.append(elemento)
    return lista

print("Configuração da lista 1:")
lista1 = criar_lista()

print("\nConfiguração da lista 2:")
lista2 = criar_lista()

lista_intercalada = []
i = 0

while i < len(lista1) and i <len(lista2):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])
    i += 1

lista_intercalada.extend(lista1[i:])
lista_intercalada.extend(lista2[i:])

print(f"\nLista intercalada:{''.join(map(str, lista_intercalada))}")

