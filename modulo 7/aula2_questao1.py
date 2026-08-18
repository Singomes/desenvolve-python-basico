from datetime import datetime


meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",
]

data_texto = input("Digite uma data de nascimento: ")

try:
    data = datetime.strptime(data_texto, "%d/%m/%Y")
    print(f"Você nasceu em {data.day:02d} de {meses[data.month - 1]} de {data.year}.")
except ValueError:
    print("Data inválida. Use o formato dd/mm/aaaa.")
