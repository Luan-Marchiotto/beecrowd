x = []

for _ in range(10):
    valor = int(input())
    x.append(valor)

for i in range(len(x)):
    if x[i] <= 0:
       x[i] = 1

    print(f'X[{i}] = {x[i]}')