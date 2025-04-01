km_pista, distancia_pedagio = map(int,input().split())

custo, valor_pedagio = map(int,input().split())

total_pista = km_pista * custo
total_pedagio = valor_pedagio * (km_pista // distancia_pedagio)

print(total_pedagio + total_pista)