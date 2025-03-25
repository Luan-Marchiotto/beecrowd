while True:
    M,N = map(int,input().split())
    
    if M == 0 and N == 0:
        exit()
    
    trocados_texto = str(M + N)
    
    print(trocados_texto.replace("0",""))