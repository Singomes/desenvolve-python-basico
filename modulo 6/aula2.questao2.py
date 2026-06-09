import random

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

soma = sum(elementos)
media = soma / num_elementos

print(f"Lista elementos: {elementos}")
print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media:.2f}")
