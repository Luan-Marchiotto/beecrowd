while True:
    soma = 0
    
    X = int(input())
    
    if X == 0:
        exit()
    
    if X % 2 == 1:
        X += 1

    for _ in range(5):
        soma += X
        X += 2
        
    print(soma)