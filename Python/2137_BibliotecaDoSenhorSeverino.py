while True:
    try:
        rep = int(input())
        cod = []
        for i in range(rep):
            palavra = input()
            cod.append(palavra)

        cod.sort()

        for ordem in cod: 
            print(ordem)
            
    except EOFError:
        break