while True:
    
    rep = int(input())
    soma_a = 0
    soma_b = 0
    
    if rep == 0:
        exit()
    
    else:  
        for i in range(rep):
            a, b = map(int,input().split())
            
            if a > b:
                soma_a +=1
            elif b > a:
                soma_b +=1
                
    print(soma_a, soma_b)