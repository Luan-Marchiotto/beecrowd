T = int(input())

N = []

for i in range(1000):
    N.append(i % T) # Adiciona somente os numeros dos restos de 0 até T-1

for i in range(1000):
    print(f'N[{i}] = {N[i]}')