while True:
    try:
        lista = input().strip()

        lado_esquerdo, resultado = lista.split('=')
        termo1, termo2 = lado_esquerdo.split('+')

        if termo1.isdigit():
            termo1 = int(termo1)
        else:
            termo1 = None
            
        if termo2.isdigit():
            termo2 = int(termo2)
        else:
            termo2 = None
            
        if resultado.isdigit():
            resultado = int(resultado)
        else:
            resultado = None
            
        ###############################    
        if termo1 is None:
            print(resultado - termo2)
        elif termo2 is None:
            print(resultado - termo1)
        elif resultado is None:
            print(termo1 + termo2)

    except EOFError:
        break