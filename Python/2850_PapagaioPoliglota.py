while True:
    try:
        estado = input()
        if estado == 'esquerda':
            print('ingles')
        elif estado == 'direita':
            print('frances')
        elif estado == 'nenhuma':
            print('portugues')
        elif estado == 'as duas':
            print('caiu')

    except EOFError:
        break