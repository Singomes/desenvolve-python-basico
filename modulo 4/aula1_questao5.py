n = int(input("Digite a quantidade de respondentes: "))

soma_idades = 0
cont = 0

while cont < n:
    idade = int(input(f"Digite a idade do respondente {cont + 1}: "))
    soma_idades += idade
    cont += 1

if n > 0:
    media = soma_idades / n
    print(f"A média de idade dos respondentes é: {media}")
else:
    print("Nenhum respondente registrado, a media é 0.")
