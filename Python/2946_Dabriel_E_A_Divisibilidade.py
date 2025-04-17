binario = input().strip()
decimal = int(binario, 2)

rep = int(input())

divisores = []

for _ in range(rep):
    m = int(input())
    if decimal % m == 0:
        divisores.append(m)

if divisores:
    print(*sorted(divisores))
else:
    print("Nenhum")