tempo = int(input())

hora = tempo // 3600  # 1 hora = 3600 segundos
tempo -= hora * 3600

minuto = tempo // 60  # 1 minuto = 60 segundos
tempo -= minuto * 60

segundo = tempo  # O restante são os segundos

# Exibe o resultado no formato HH:MM:SS
print('{}:{}:{}'.format(hora, minuto, segundo))
