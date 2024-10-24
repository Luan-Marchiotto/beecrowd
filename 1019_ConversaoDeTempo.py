tempo = int(input())

hora = tempo // 3600
tempo -= hora * 3600

minuto = tempo // 60
tempo -= minuto * 60

segundo = tempo

print('{}:{}:{}'.format(hora, minuto, segundo))