rep = int(input())

numeros = list(map(int, input().split()))

cont2 = cont3 = cont4 = cont5 = 0

for n in numeros:
    if n % 2 == 0:
        cont2 += 1
    if n % 3 == 0:
        cont3 += 1
    if n % 4 == 0:
        cont4 += 1
    if n % 5 == 0:
        cont5 += 1

print(f"{cont2} Multiplo(s) de 2")
print(f"{cont3} Multiplo(s) de 3")
print(f"{cont4} Multiplo(s) de 4")
print(f"{cont5} Multiplo(s) de 5")