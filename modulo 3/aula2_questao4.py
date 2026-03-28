classe = input("Escolha a classe (guerreiro, mago ou arqueiro):")
força = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))
consistente = False

if classe == "guerreiro":
     if força >= 15 and magia <= 10:
         consistente = True

if classe =="mago":
     if força <= 10 and magia >= 15:
          consistente = True

if classe == "arqueiro":
     if força > 5 and força <= 15 and magia > 5 and magia<= 15:
          consistente = True

print(f"Pontos de atributos consistentes com a classe escolhida: {consistente}")



