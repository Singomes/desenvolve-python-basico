# Leitura de dados (entrada)
# Ler o comprimento do terreno como número inteiro
comprimento = int(input("Digite aqui o comprimento do terreno (m): "))

# Ler largura do terreno com número inteiro
largura = int(input("Digite aqui a largura do terreno (m): "))

# Ler o preço do metro quadrado como número flutuante
preco_m = float(input("Digite o preco do metro aqui (R$): "))

# Processamento
# Calcular a área do terreno em metros quadrados
area_m = comprimento * largura

#Calcular preço total do terreno
preco_total = preco_m * area_m

# Impressão de dados
# Imprimir o resultado formatando valor monetário com duas casas decimais
print(f"o terreno possui {area_m})m2 e custa R$ {preco_total:,.2f}")

 