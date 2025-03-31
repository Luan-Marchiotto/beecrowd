while True:
    rep = int(input())
    
    if rep == 0:
        break 
    
    lista = list(map(int, input().split()))
    
    mary = lista.count(0)
    john = lista.count(1)
    
    print(f"Mary won {mary} times and John won {john} times")