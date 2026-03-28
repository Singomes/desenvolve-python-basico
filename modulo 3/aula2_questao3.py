idade = int(input("Digite sua idade: " ))

jogados = input("já jogou pelo menos 3 jogos? (True/False) ") == 'True'

vitorias = int(input("Quantos jogos já venceu? "))

apto = (16 <= idade <= 18) and (jogados == True) and (vitorias >= 1)

print(f"apto para infressar no clube de jogos de tabuleiro: {apto}")



