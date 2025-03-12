while True:
    try:
        reclamacao = int(input())
        
        if reclamacao == 0:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
    except EOFError:
        break