n = int(input("Digite a quantidade de números (n): "))
maior = 0

while n>0:
    x = int(input("Digite o número (x): "))

    if x>maior:
        maior=x

        n = n-1

print(f"O maior valor digitado foi:{maior}")


