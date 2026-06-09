import random

lista1 = [random.randint(0, 50)for _ in range(20)]
lista2 = [random.randint(0, 50)for _ in range(20)]

interseccao = sorted(list(set(lista1) & set(lista2)))

print(f"lista1 = {lista1}")
print(f"lista2 = {lista2}")
print(f"Interseccao = {interseccao}")

print("\nContagem:")
for valor in interseccao:
    qtd1 = lista1.count(valor)
    qtd2 = lista2.count(valor)
    print(f"{valor}: (lista1={qtd1}, lista2={qtd2})")
