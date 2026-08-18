def validador_senha(senha):
    tem_tamanho_minimo = len(senha) >= 8
    tem_maiuscula = any(caractere.isupper() for caractere in senha)
    tem_minuscula = any(caractere.islower() for caractere in senha)
    tem_numero = any(caractere.isdigit() for caractere in senha)
    tem_especial = any(not caractere.isalnum() for caractere in senha)

    return (
        tem_tamanho_minimo
        and tem_maiuscula
        and tem_minuscula
        and tem_numero
        and tem_especial
    )


# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # True
print(validador_senha(senha2))  # False
print(validador_senha(senha3))  # False
