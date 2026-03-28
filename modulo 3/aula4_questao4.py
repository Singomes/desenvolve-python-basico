distancia = float(input("Digite a distancia em Km: "))
peso = float(input("Digite o peso em Kg: "))
if distancia <= 100:
    valor_por_kg = 1.00
elif distancia <= 300:
    valor_por_kg = 1.50
else:
    valor_por_kg = 2.00

frete_total = peso * valor_por_kg

if peso > 10:
    frete_total += 10.00

print(f"O valor do frete  é: R${frete_total:.2f}")

