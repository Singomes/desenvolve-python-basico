total_compra = 0

nome = input(f"Digite o nome do produto 1: ")
preco = float(input(f"Digite o preço unitário do produto: "))
quantidade = int(input(f"Digite a quantidade do produto: "))
total_compra += preco * quantidade 

nome = input(f"Digite o nome do produto 2: ")
preco = float(input(f"Digite o preço unitário do produto: "))
quantidade = int(input(f"Digite a quantidade do produto: "))
total_compra += preco * quantidade 

nome = input(f"Digite o nome do produto 3: ")
preco = float(input(f"Digite o preço unitário do produto: "))
quantidade = int(input(f"Digite a quantidade do produto: "))

total_compra += preco * quantidade 

print(f"Total: R${total_compra:,.2f}")
