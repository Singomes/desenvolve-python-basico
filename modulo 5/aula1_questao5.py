import emoji

print("Emojis disponíveis: ")
print(" - : red_heart:")
print(" - :thumbs_up:")
print(" - :thinking_face:")
print(" - :partying_face:")

frase_codificada = input("\nDigite uma frase e ela será emojizada: ")

frase_emojizada = emoji.emojize(frase_codificada, language='alias')

print(f"Frase emojizada: {frase_emojizada}")
