x, y = list(map(int, input().split()))
cont = 1

for _ in range(1, int(y/x)+1):
    msg = ""
    
    for _ in range(x):
        msg += str(cont)+" "
        cont+=1
        
    print(msg[:-1])