n = int(input("Digite: "))

cont = 0
soma_coelhos = 0
soma_ratos = 0
soma_sapos = 0
total_cobais = 0

while cont < n:
    quantia = int(input("Digite: "))
    tipo = input()

    total_cobais += quantia

    if tipo == 'c': 
        soma_coelhos += quantia
    elif tipo == 'r':
        soma_ratos += quantia
    elif tipo == 's':
        soma_sapos += quantia

    cont += 1


print("Total cobaias: " , soma_coelhos + soma_ratos + soma_sapos)
print("Total de coelhos: " , soma_coelhos)
print("Total de ratos: " , soma_ratos)
print("Total de sapos: ", soma_sapos)
print("Percentual de coelhos: ", (soma_coelhos/n) * 100)
print("Percentual de ratos: ", (soma_ratos/n) * 100)
print("Percentual de sapos: ", (soma_sapos/n) * 100)
