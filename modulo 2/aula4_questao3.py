total_compra = 0

nome = input(f"Digite o nome do produto: ")
preco = float(input(f"Digite o preço unitário do produto: "))
quantidade = int(input(f"Digite a quantidade do produto: "))

total_compra += preco * quantidade 

total_formatado = f"{total_compra:,.2f}".replace(",","x").replace("x",".")

print(f"\nTotal: R${total_formatado}")
