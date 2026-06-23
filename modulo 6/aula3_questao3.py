import random
lista = [random.randint(-10, 10) for_in range(20)]
print(f"Original: {lista}")

max_negativos = 0
inicio_del, fim_del = 0, 0

for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        sublista = lista[i:j]

        if all(n<0 for n in sublista):
            if len(sublista) > max_negativos:
                max_negativos = len(sublista)
                inicio_del, fim_del = i, j

if max_negativos > 0:
    del lista[inicio_del:fim_del]

print(f"Editada: {lista}")

