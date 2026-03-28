genero = input("Digite seu genero: (M/F)")
idade = int(input("Digite sua idade: "))
tempo_serviço = int(input("Digite o tempo de serviço: "))

aposentar = ((genero == 'M' and idade >65) or (genero == 'F' and idade > 60)) or (tempo_serviço >= 30) or (idade >= 60 and tempo_serviço >= 25)
print(aposentar)
