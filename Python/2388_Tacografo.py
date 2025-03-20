rep = int(input())
distancia = 0

for _ in range(rep):
    horas, velocidade = map(int,input().split())
    
    distancia += horas * velocidade

print(distancia)