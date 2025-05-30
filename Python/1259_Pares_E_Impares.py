rep = int(input())

numeros = []
pares = []
impares = []

for _ in range(rep):
    numeros.append(int(input()))
    
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

pares.sort()
impares.sort(reverse=True)

for num in pares + impares:
    print(num)