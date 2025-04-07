estado = input()

regiao = {
    'para': "Regiao Norte",
    'acre': "Regiao Norte",
    'roraima' : "Regiao Norte",
    'amapa' : "Regiao Norte",
    'amazonas' : "Regiao Norte",
    'rondonia' : "Regiao Norte",
    'tocantins' : "Regiao Norte",
}

if estado in regiao:
    print(regiao[estado])
    
else:
    print("Outra regiao")