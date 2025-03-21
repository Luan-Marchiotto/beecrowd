while True:
    soma_nota = 0
    cont = 0

    while cont < 2:
        x = float(input())

        if x >= 0 and x <= 10:
            soma_nota += x
            cont += 1
        else:
            print("nota invalida")

    print(f"media = {soma_nota / 2:.2f}")

    while True:
        print("novo calculo (1-sim 2-nao)")
        escolha = int(input())
        if escolha == 1:
            break
        elif escolha == 2:
            exit()