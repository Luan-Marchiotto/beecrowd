import re

rep = int(input())

for _ in range(rep):
    texto = input()
    
    numeros_encontrados = re.findall(r'\d+', texto)
    
    numeros_int = list(map(int, numeros_encontrados))
    
    print(sum(numeros_int))