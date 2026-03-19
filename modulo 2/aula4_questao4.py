valor = int(input)

valor_restante = valor

notas = [100, 50 , 20, 10, 5, 2, 1]

print(valor)

for nota in notas:
 quantidade_notas = valor_restante// nota
 valor_restante = valor_restante % nota

print(f"{quantidade_notas} nota(s) de R${nota},00")

