rapido, lento = map(int,input().split())

volta = 0
diferenca = 0 

while True:

    diferenca += lento - rapido
    
    if diferenca > lento - 1:
        break
    
    volta +=1
    
print(volta + 1)