from datetime import datetime

agora = datetime.now()

print(f"Data: {agora.strftime('%d/%m/%Y')}")
print(f"Hora: {agora.strftime('%H:%M')}")
