rep = int(input())

for _ in range(rep):
    hora, minuto, acao = map(int,input().split())

    if acao == 0:
        print(f"{hora:02}:{minuto:02} - A porta fechou!")
        
    elif acao == 1:
        print(f"{hora:02}:{minuto:02} - A porta abriu!")