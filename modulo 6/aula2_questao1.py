import random

lista_original = [random.randint(-100, 100) for i in range(20)]

lista_ordenada = sorted(lista_original)

indice_maior = lista_original.index(max(lista_original))
indice_menor = lista_original.index(min(lista_original))

print(f"a lista ordenada: {lista_ordenada}")
print(f"A lista original: {lista_original}")
print(f"O índice do maior valor da lista: {indice_maior}")
print(f"O índice menor valor da lista: {indice_menor}")