cont = 0
soma = 0
for i in range(6):
    x = float(input())
    
    if x > 0:
        cont += 1
        soma += x
        
print(f"{cont} valores positivos")
print(f"{soma/cont:.1f}")