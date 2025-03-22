casos_teste = int(input())

for _ in range(casos_teste):
    quantidade_de_pessoas = int(input())

    idioma = input()
    mesmoIdioma = True
    
    for i in range(1, quantidade_de_pessoas):
        lingua = input()
        
        if(lingua != idioma):
            mesmoIdioma = False
    
    if mesmoIdioma == False:
        print("ingles")
        
    elif mesmoIdioma == True:
        print(idioma)